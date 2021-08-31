import math


def is_square(number):
    if type(number) != int:
        raise ValueError("Please provide a valid integer.")

    if number < 0:
        return False

    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return True
    else:
        return False