# Parse books

The present script - ```parse_books.py``` allows to download books datas (book title, genre, comments, cover, book text) from inputed link. This script parse the books from inputed interval ```id```. The books ID interval entered at the same time when the code is run, in command line.
So, this script is a classic parser HTML pages.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

For correctly script work, you must create ```.env``` file in the script directory.
This file have to consider one line with parsing URL. The example of this line below:
```
URL_FOR_DOWNLOADING=https://tululu.org/
```
For script running you have to start the command line and change directory to the code containing.
The next step is start the script for this template:
```
[full_dir_path] python parse_books.py [start_book_id] [end_book_id]
```
For example: 
```
d:\CODING\DEVMAN\Online_Library>python parse_books.py 20 30
```

### Output results

As results you get ```.txt``` files with books content to ```/books/``` directory.
Also the books cover images downloads to ```/images/``` directory.
You don't have to create these directories before. 

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).