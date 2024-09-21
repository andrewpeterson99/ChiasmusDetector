#A script to remove all empty lines from a text file.
#also removes leading tabs/white spaces and trailing white spaces

import sys

def clean_text(file_path):
    #copy the file first
    new_file_path = file_path.replace('.txt', '_clean.txt')
    with open(file_path, 'r') as f:
        with open(new_file_path, 'w') as f2:
            for line in f:
                stripped_line = line.strip()
                #if line is empty
                if stripped_line == '':
                    continue
                f2.write(stripped_line + '\n')
    return new_file_path

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python clean_text.py <file_path>')
        sys.exit(1)
    file_path = sys.argv[1]
    new_file_path = clean_text(file_path)
    print('Cleaned text saved to:', new_file_path)