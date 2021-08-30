def ensure(word):
    return word if word != '' and word[-1] == '?' else f'{word}?'