def prev_mult_of_three(number):
    if type(number) != int:
        raise ValueError(f"{number} with type ({type(number)}) is not a valid integer.")
    word_number = str(number)
    while len(word_number) != 1:
        is_divisible =  int(word_number) % 3 == 0
        if is_divisible:
            return int(word_number)
        else:
            word_number = word_number[0:len(word_number) - 1]

    if len(word_number) == 1 and int(word_number) % 3 == 0:
        return int(word_number)