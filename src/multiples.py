def multiple(number):
    if type(number) != int:
        raise ValueError('Please provide a valid integer.')

    message = ''
    if number % 3 == 0:
        message = 'Bang'
    if number % 5 == 0:
        message += 'Boom'
    if number % 3 != 0 and number % 5 != 0:
        message = 'Miss'
    return message