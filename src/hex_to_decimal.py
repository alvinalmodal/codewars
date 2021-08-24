def hex_to_dec(value):
    try:
        return int(value, 16)
    except:
        raise ValueError(f"Unable to convert {value}. Please provide a valid string integer.")