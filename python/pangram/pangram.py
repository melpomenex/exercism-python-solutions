import string

def is_pangram(word):
    return all(c in word.lower() for c in string.ascii_lowercase)
