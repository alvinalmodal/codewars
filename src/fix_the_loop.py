def list_animals(animals):
    if type(animals) != list:
        raise ValueError(f'{animals} with type of {type(animals)} is not a valid list of animals.')
    message = ''
    for i, animal in enumerate(animals):
        message += f'{i + 1}. {animal}\n'
    return message