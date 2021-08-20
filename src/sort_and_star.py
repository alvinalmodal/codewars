def two_sort(array):
    if type(array) != list or len(array) == 0:
        raise ValueError('Please provide a list of values.')
    return "***".join(min(array))