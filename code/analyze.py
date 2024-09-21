# This file consumes chunks of text from a file at a time and processes them.
# The processing uses llm.py to determine if the chunk is a chiasmus.
# If it is a chiasmus, it writes the chunk to a new file along with the certainty level.

from llm import LLM
import sys

model = LLM()
#TODO: implement scaling CHUNK_SIZE
CHUNK_SIZES = [10, 20, 30, 40, 50] #this may need to be fine tuned

def consume_chunk(position, book_file) -> tuple(str, int):
    with open(book_file, 'r') as f:
        lines = f.readlines()
    #get the nearest complete sentence for the chunk
    chunk = ' '.join(lines[position:position+CHUNK_SIZES[0]])
    #check if the chunk is a chiasmus
    certainty_score = model.prompt(chunk)
    return (chunk, certainty_score)

def process_book(book_file):
    with open(book_file, 'r') as f:
        lines = f.readlines()
    book_length = len(lines)
    position = 0
    while position < book_length:
        (chunk, certainty_score) = consume_chunk(position, book_file)
        if certainty_score >= 5:
            #write the chunk to a new file
            with open(book_file, 'a') as f:
                f.write(chunk)
        position += CHUNK_SIZES[0]

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python analyze.py <book_file>')
        sys.exit(1)-
    book_file = sys.argv[1]
    process_book(book_file)
    print('Chiasmus chunks saved to individual files.')