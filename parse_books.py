import os
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathvalidate import sanitize_filename

  
def get_response(url, header=None):
    response = requests.get(url, params=header, allow_redirects=False)
    response.raise_for_status()

    return response

def check_for_redirect(response):
    if response.status_code != 200:
       raise HTTPError
    else:
       pass

def get_book_title(url, book_id):
    url = f'{url}b{book_id}/'
    response = get_response(url)
    try:
        check_for_redirect(response)
    except:
        return
    soup = BeautifulSoup(response.text, 'lxml')
    book_name_and_author = soup.find(id = 'content').find('h1')
    book_title = book_name_and_author.get_text().split('::')[0].strip()

    return book_title

def create_filename(book_title, book_id):
    filename = f'{sanitize_filename(book_title)}.txt'
    filename = f'{book_id}_{filename}'

    return filename

def create_filepath(filename, folder='books'):
    filepath = os.path.join(folder, filename)

    return filepath

def download_txt(url, filepath):
    url = f'{url}txt.php'
    response = get_response(url, header={'id': book_id})
    try:
        check_for_redirect(response)
    except:
        return
    with open(filepath, 'w', encoding='utf-8') as file: file.write(response.text)

        
if __name__ == '__main__':
    load_dotenv()
    url = os.getenv('URL_FOR_DOWNLOADING')
    os.makedirs('books', exist_ok=True)

    books_number = 10

    for book_id in range(1, books_number+1):
        book_title = get_book_title(url, book_id)
        if book_title:
            filename = create_filename(book_title, book_id)
            filepath = create_filepath(filename, folder='books')
        else:
            continue
        
        download_txt(url, filepath)   
        