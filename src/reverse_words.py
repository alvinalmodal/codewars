def reverse(sentence):
    if type(sentence) != str:
        raise ValueError('Please provide a valid string input.')
    return " ".join(sentence.split(' ')[::-1])