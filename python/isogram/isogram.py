import re

def is_isogram(string):
    """
    Determine if a word or phrase is an isogram.

    An isogram is a word or phrase without a repeating letter.
    """
    string = string.lower()
    pattern = re.compile(r"([a-z]).*\1")
    return not bool(pattern.search(string))
