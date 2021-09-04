import math

def is_prime(number):

    if type(number) != int:
        raise ValueError(f"{number} with type({type(number)} is not a valid integer.")

    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False

    sqrt = int(math.sqrt(number)) + 1

    for divisor in range(3, sqrt, 2):
        if number % divisor == 0:
            return False

    return True