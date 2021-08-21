def remove(words):
    if type(words) != str or len(words) == 0:
        raise ValueError('Please provide a valid string')
    return words.rstrip('!')