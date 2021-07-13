# DSC510
# Week 8
# 8.1 Programming Assignment
# Author Michelle Rice
# 10/22/20
# This program opens a text file and counts the words in the file
# and prints a list of each word and how many times that word occurs
import string
filename = input("What would you like to name your file?")


# The process_line function looks at the file line by line and processes
# each word. Strip punctuation, do not count --, convert all words to lower case
# Calls the add_word function to add words that meet the criteria to the dictionary
def process_line(line, word_count_dict):
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        if word != '--':
            word = word.lower()
            word = word.strip()
            word = word.strip(string.punctuation)
            add_word(word, word_count_dict)


# The add_word function is called by the process_line function
# and adds each word to the dictionary
def add_word(word, word_count_dict):
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


# The pretty_print function is to separate out the formatting and printing
# Print the list in high to low frequency order
def pretty_print(word_count_dict):
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    print('\n''{:15s}{:15s}'.format("Word", "Count"))
    print('-'*20)
    for val, key in value_key_list:
        print('{:15s} {:<3d}'.format(key, val))


# The process_file function writes to a new file
def process_file(word_count_dict):
    value_key_list = []
    for key, val in word_count_dict.items():
        value_key_list.append((val, key))
    value_key_list.sort(reverse=True)
    with open(filename, 'w') as fileHandle:
        fileHandle.write('\n''{:15s}{:15s}'.format("Word", "Count"))
        fileHandle.write('\n')
        for val, key in value_key_list:
            fileHandle.write('\n''{:15s}{:<3d}'.format(key, val))


# the main function opens the file and calls the process_line function
# and prints the length of the dictionary
def main():
    word_count_dict = {}
    try:
        gba_file = open('gettysburg.txt', 'r')
    except FileNotFoundError as e:
        print(e)
    for line in gba_file:
        process_line(line, word_count_dict)
    with open(filename, 'w') as fileHandle:
        print('Length of the dictionary:', len(word_count_dict))
    # pretty_print(word_count_dict)
    process_file(word_count_dict)


if __name__ == "__main__":
    main()
