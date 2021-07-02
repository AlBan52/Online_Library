import os
import requests

from dotenv import load_dotenv

  
def check_for_redirect(response):
    if response.status_code != 200:
       raise HTTPError
    else:
       pass

        
if __name__ == '__main__':
    load_dotenv()
    url = os.getenv('URL_FOR_DOWNLOADING')
    os.makedirs('books', exist_ok=True)

    books_number = 10

    for book_id in range(1, books_number+1):
        response = requests.get(url, params={'id': book_id}, allow_redirects=False)
        response.raise_for_status()
        try:
            check_for_redirect(response)
        except:
            continue

        with open(f'books/{book_id}.txt', 'w', encoding='utf-8') as file:
            file.write(response.text)
        