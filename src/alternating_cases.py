def to_alternating_case(word):
    if type(word) != str:
        raise ValueError('Please provide a valid string/word.')
    return word.swapcase()