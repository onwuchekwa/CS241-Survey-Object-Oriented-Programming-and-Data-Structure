import re

def prompt_filename():
    return input('Please enter the filename: ')

def prompt_word():
    return input('Please enter any word: ')

def parse_file(filename):
    word_count = 0
    new_word = prompt_word()
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                #if (word == "pride"):
                #if (word.lower() == "pride"):
                if (word.lower() == new_word.lower()):
                    word_count += 1
    return word_count
    
def main():
    open_file = prompt_filename()
    print("Opening file '{}'".format(open_file))
    word_count = parse_file(open_file)
    print("The word pride occurs {} times in this file.".format(word_count))
    
if __name__ == "__main__":
    main()