import os
import requests


url = 'https://tululu.org/txt.php'

os.makedirs('books', exist_ok=True)

book_id = 1
books_number = 10

while book_id <= books_number:
    response = requests.get(url, params={'id': book_id})
    response.raise_for_status()

    with open(f'books/{book_id}.txt', 'w', encoding='utf-8') as file:
        file.write(response.text)
    book_id += 1
    