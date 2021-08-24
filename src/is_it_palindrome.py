def is_palindrome(word):
    if type(word) != str:
        raise ValueError(f'{word} with type {type(word)} is not a valid string.')
    return word.lower() == word.lower()[::-1]