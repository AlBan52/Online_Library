import os
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv

  
def get_response(url, header):
    response = requests.get(url, params=header, allow_redirects=False)
    response.raise_for_status()

    return response

def check_for_redirect(response):
    if response.status_code != 200:
       raise HTTPError
    else:
       pass

def download_txt(url, filename, folder='books'):
    response = get_response(url, header)
    filename = f'{sanitize_filename(filename)}.txt'
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w', encoding='utf-8') as file: file.write(response.text)

    return filepath
        
if __name__ == '__main__':
    load_dotenv()
    url = os.getenv('URL_FOR_DOWNLOADING')
    os.makedirs('books', exist_ok=True)

    books_number = 10

    for book_id in range(1, books_number+1):
        header = {'id': book_id}
        response = get_response(url, header)
        
        try:
            check_for_redirect(response)
        except:
            continue

        with open(f'books/{book_id}.txt', 'w', encoding='utf-8') as file:
            file.write(response.text)
        