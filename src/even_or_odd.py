def check_number(number):
    if type(number) != int:
        raise ValueError("Please provide a valid integer.")
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"