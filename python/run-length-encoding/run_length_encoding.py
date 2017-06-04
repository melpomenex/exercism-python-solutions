from itertools import groupby
from re import findall

def decode(compressed):
    ''' decompresses the string '''
    return ''.join(
        int(count) * letter if count else letter
        for count, letter in findall('(\d*)(.)', compressed ))


def encode(letters):
    ''' compresses text by replacing repeated characters '''
    encoded = ''
    for char, group in groupby(letters):
        length = len(list(group))
        if length > 1:
            encoded += str(length)
        encoded += char
    return encoded
