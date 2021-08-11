import argparse
import os
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pathvalidate import sanitize_filename
from urllib.parse import urljoin

  
def parse_books_interval():
    parser = argparse.ArgumentParser()
    parser.add_argument('start_book_id', type=int)
    parser.add_argument('end_book_id', type=int)
    args = parser.parse_args()
    start_book_id = args.start_book_id
    end_book_id = args.end_book_id
    return start_book_id, end_book_id

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

def download_txt(url, book_title, folder='books'):
    os.makedirs('books', exist_ok=True)
    url = f'{url}txt.php'
    filename = f'{sanitize_filename(book_title)}.txt'
    filename = f'{book_id}_{filename}'
    filepath = os.path.join(folder, filename)
    response = get_response(url, header={'id': book_id})
    try:
        check_for_redirect(response)
    except:
        return
    with open(filepath, 'w', encoding='utf-8') as file: file.write(response.text)

def get_image_link(url, book_id):
    url = f'{url}b{book_id}/'
    response = get_response(url)
    try:
        check_for_redirect(response)
    except:
        return
    soup = BeautifulSoup(response.text, 'lxml')
    image_link = soup.find(id = 'content').find('img')['src']
    full_image_link = urljoin(url, image_link)
     
    return full_image_link

def download_images(full_image_link, folder='images'):
    os.makedirs('images', exist_ok=True)
    url = full_image_link
    image_name = full_image_link.split('/')[-1]
    image_path = os.path.join(folder, image_name)
    response = get_response(url)
    try:
        check_for_redirect(response)
    except:
        return
    with open(image_path, 'wb') as file: file.write(response.content)

def get_comments(url):
   url = f'{url}b{book_id}/'
   response = get_response(url)
   try:
      check_for_redirect(response)
   except:
      return
   soup = BeautifulSoup(response.text, 'lxml')
   raw_comments = soup.find_all(class_='texts')
   
   comments_texts = []
   for comment in raw_comments:
      comment = comment.find('span').text
      comments_texts.append(comment)
       
   return comments_texts

def get_book_genres(url):
   url = f'{url}b{book_id}/'
   response = get_response(url)
   try:
      check_for_redirect(response)
   except:
      return
   soup = BeautifulSoup(response.text, 'lxml')
   raw_book_genres = soup.find('span', class_='d_book').find_all('a')
   
   book_genres = []
   for genre in raw_book_genres:
      genre = genre.text
      book_genres.append(genre)
      
   return book_genres        

def parse_book_page(url):
   book_title = get_book_title(url, book_id)
   book_genres = get_book_genres(url)
   comments_texts = get_comments(url)
   about_book = {'Название': book_title,
                 'Жанр': book_genres,
                 'Комментарии': comments_texts
                 }

   return book_title, about_book


if __name__ == '__main__':
    load_dotenv()
    url = os.getenv('URL_FOR_DOWNLOADING')
    start_book_id, end_book_id = parse_books_interval()
    
    for book_id in range(start_book_id, end_book_id+1):
        book_title, about_book = parse_book_page(url)
        full_image_link = get_image_link(url, book_id)
        if book_title and about_book:
            download_txt(url, book_title, folder='books')
            download_images(full_image_link, folder='images')
        else:
            continue
        
           
        