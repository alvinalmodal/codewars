def generate_range(min, max, step):
    if type(min) != int:
        raise ValueError('Please provide a valid integer for min.')
    if type(max) != int:
        raise ValueError('Please provide a valid integer for max.')
    if type(step) != int:
        raise ValueError('Please provide a valid integer for step.')
    return [number for number in range(min, max + 1, step)]