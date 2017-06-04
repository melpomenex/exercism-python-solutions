def hey(phrase):
    phrase = phrase.strip()
    if phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase.endswith('?'):
        return 'Sure.'
    elif phrase == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
