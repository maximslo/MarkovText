#
# Markov text generator using dictionaries
#
# How to import text: word_dict = create_dictionary('filename.txt')
# How to generate text: generate_text(word_dict, lenth of generated text)
#

import random
def create_dictionary(filename):
    """Creates a dictionary with each word as a key and a list of words after it as their value."""
    content = open(filename, 'r')
    source = []
    
    for x in content:
        mylist = x.split(' ')
        mylist[-1] = mylist[-1][:-1]
        if mylist[-1] == '':
            mylist = mylist [:-1]
            source += mylist
            continue
        source += mylist
        
    mydictionary = {}
    current = '$'
    for word in source:
        if current not in mydictionary:
            mydictionary[current] = [word]
        else:
            mydictionary[current] += [word]
        if word[-1] in '!.?':
            current = '$'
        else:
            current = word
    return mydictionary

def is_end(s):
    """A helper function that determines if a word is the end of a sentence."""
    return s[-1] in '!.?'

def generate_text(word_dict, num_words):
    """Generates a text using a dictionary and prints a text with the specified length."""
    current = '$'
    for x in range(num_words):
        wordlist = word_dict[current]
        nextword = random.choice(wordlist)
        if is_end(nextword):
            current = '$'
        else:
            current = nextword
        print(nextword, end = ' ')
