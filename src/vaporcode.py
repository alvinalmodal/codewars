def vaporize(word):
    if type(word) != str:
        raise ValueError(f'{word} with type of {type(word)} is not a string.')
    return "  ".join([character.upper() for character in word.replace(' ','')])