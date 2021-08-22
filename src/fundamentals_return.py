def is_a_number(arg):
    if not (type(arg) == int or type(arg) == float):
        return False
    return True


def validate_numeric(func):
    def validate_numeric_wrapper_func(*args, **kwargs):
        for arg in args:
            if not is_a_number(arg):
                raise ValueError(f'{arg} is not a valid number.')
        return func(*args, **kwargs)
    return validate_numeric_wrapper_func

@validate_numeric
def add(*args):
    return sum(args)


@validate_numeric
def subt(num1, num2):
    return num1 - num2


@validate_numeric
def multiply(num1, num2):
    return num1 * num2


@validate_numeric
def divide(num1, num2):
    return num1 / num2


@validate_numeric
def mod(num1, num2):
    return num1 % num2


@validate_numeric
def exponent(num1, num2):
    return num1 ** num2
