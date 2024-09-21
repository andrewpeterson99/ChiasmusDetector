import sys
import os

DO_NOT_WRITE_BOOK_TITLES = [
    "Mormon's abridgement",
    "The small plates of Nephi",
    "Moroni's additions"
]

def make_book_files(mass_text):
    book_name = ''
    book_text = ''
    
    #put all the books in a folder called 'books'
    if not os.path.exists('books'):
        os.makedirs('books')

    for line in mass_text:
        if line[0] != ' ':
            if book_name and book_name not in DO_NOT_WRITE_BOOK_TITLES:
                with open(f'books/{book_name}.txt', 'w') as f:
                    #remove first line from book_text
                    f.write(book_text[1:])
            book_name = line.strip()
            book_text = ''
        else:
            book_text += line
    if book_name:
        with open(f'books/{book_name}.txt', 'w') as f:
            f.write(book_text)

    #remove the first line of every file in the books folder
    for file_name in os.listdir('books'):
        with open(f'books/{file_name}', 'r') as f:
            lines = f.readlines()
        with open(f'books/{file_name}', 'w') as f:
            f.write(''.join(lines[1:]))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python chunk_text.py <file_path>')
        sys.exit(1)
    file_path = sys.argv[1]
    with open(file_path, 'r') as f:
        mass_text = f.readlines()
    make_book_files(mass_text)
    print('Books saved to individual files.')