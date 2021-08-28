def validate_change_vowels_input(sentence, replacement_vowel, vowel_list):
    if type(sentence) != str:
            raise ValueError(f"{sentence} with type {type(sentence)} is not a string.")
    if type(replacement_vowel) != str:
        raise ValueError(f"{replacement_vowel} with type {type(replacement_vowel)} is not a string.")
    if replacement_vowel not in vowel_list:
        raise ValueError(f"{replacement_vowel} is not a valid vowel. Please refer to {vowel_list} as an example.")


def change_vowels(sentence, replacement_vowel):
    vowels = ['a', 'e', 'i', 'o', 'u']
    validate_change_vowels_input(sentence, replacement_vowel, vowels)    
    return "".join([replacement_vowel if character in vowels else character for character in sentence ])
    