def two_sort(array):
    if type(array) != list or len(array) == 0:
        raise ValueError('Please provide a list of values.')
    sorted_values = sorted(array)
    return add_star(sorted_values[0])


def add_star(word):
    letters = list(word)
    return "***".join(letters)