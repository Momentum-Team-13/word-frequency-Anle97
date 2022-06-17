import string

from bleach import Cleaner

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

#empty dictionaries to be populated
word_dict = {}
organized_dict = {}

#function to count words/populate dictionaries
def count_words(text):
    #counts the number of words and puts into word_dict
    for word in text:
        if word_dict.get(word) == None:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    #creates a new dictionary that sorts word_dict
    organized_list = sorted(word_dict, key=word_dict.get, reverse=True)
    for key in organized_list:
        organized_dict[key] = word_dict[key]
    #prints the values of organized_dict
    for key, value in organized_dict.items():
        stars = ""
        for i in range(value):
            stars += '*'
        print(f'{key:>14} | {value} | {stars}')


# function that opens file and prints output in python console
def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    print(f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.read()
        # makes text lowercase, removes punctuation and makes string into a list
        clean_file = read_file.translate(str.maketrans('', '', string.punctuation)).lower().split()
        # removes stop words
        cleanest_file = [word for word in clean_file if word not in STOP_WORDS]     
    #calls function on cleaned file to print output
    count_words(cleanest_file)



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
