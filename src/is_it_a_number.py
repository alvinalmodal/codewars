def is_digit(value):
    try:
        value_to_convert = value.strip() if type(value) == str else value
        float(value_to_convert)
        return True
    except:
        return False
