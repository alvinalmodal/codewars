def shuffle(name):
    if type(name) != str:
        raise ValueError(f"{name} with type {type(name)} is not a string")
    first,last = name.split(' ')
    return f'{last} {first}'