def sum_digits(digits):
    if digits == None:
        return ""

    _digits = digits[:] if type(digits) == str else str(digits)
    converted_digits = [int(digit) for digit in _digits]
    return f"{' + '.join(_digits)} = {sum(converted_digits)}"
    