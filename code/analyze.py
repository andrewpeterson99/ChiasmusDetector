# This file consumes chunks of text from a file at a time and processes them.
# The processing uses llm.py to determine if the chunk is a chiasmus.
# If it is a chiasmus, it writes the chunk to a new file along with the certainty level.

from llm import LLM

model = LLM()
CHUNK_SIZES = [10, 20, 30, 40, 50] #this may need to be fine tuned

def consume_chunk(position, book_file):
    with open(book_file, 'r') as f:
        lines = f.readlines()
    #get the nearest complete sentence for the chunk
    chunk = ' '.join(lines[position:position+CHUNK_SIZES[0]])
    #check if the chunk is a chiasmus
    model.prompt(chunk)
    return
