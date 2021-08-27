def sentence_converter(words):
    if type(words) != list:
        raise ValueError(f'{words} with type {type(words)} is not a valid list.')
    return " ".join(words)

