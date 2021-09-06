def swap_vowel_case(word):
    if type(word) != str:
        raise ValueError('Please provide a valid string.')
        
    vowels = 'aeiou'
    return "".join([char if char.lower() not in vowels else char.swapcase() for char in word])