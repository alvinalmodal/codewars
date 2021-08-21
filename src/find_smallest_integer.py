def find_smallest_int(numbers):
    if type(numbers) != list or len(numbers) == 0:
        raise ValueError('Please provide a valid list of numbers.')
    return min(numbers)