import re
from collections import Counter


def word_count(phrase):
    ''' returns the number of occurences of each word in a given phrase '''
    return Counter(word.lower() for word in re.split('[_\W]+', phrase) if word)
