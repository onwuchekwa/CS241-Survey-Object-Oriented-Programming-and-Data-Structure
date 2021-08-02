# Function to prompt the user for file
def prompt_filename():
    return input('Enter file: ')

# Function to open file
def open_file(file_path, open_type):
    return open(file_path, open_type)

# Function to open file, count the number of lines and word and print result
def main():
    prompt = prompt_filename()
    file = open_file(prompt, 'r')
    line_count = 0
    word_count = 0
    for line in file:
        line_count += 1
        word_count += len(line.split(' '))
    print('The file contains {0} lines and {1} words.'.format(line_count, word_count))    

if __name__ == "__main__":
    main()
    