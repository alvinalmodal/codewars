def boolean_to_string(boolean_value):
    if type(boolean_value) != bool:
        raise ValueError("Please provide a valid boolean value (True/False)")
    return str(boolean_value)