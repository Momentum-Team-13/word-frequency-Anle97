import string

from bleach import Cleaner

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

words = []
word_dict = {}

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.read()
        # makes text lowercase, removes punctuation and makes string into a list
        clean_file = read_file.translate(str.maketrans('', '', string.punctuation)).lower().split()
        # removes stop words
        cleanest_file = [word for word in clean_file if word not in STOP_WORDS] 
    
    print(cleanest_file)
    print(len(cleanest_file))






if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
