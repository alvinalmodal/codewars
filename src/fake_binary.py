def fake_bin(number_string):
    try:
        int(number_string)
    except:
        raise ValueError("Unable to convert string to int. Please provide a valid integer.")
    return ''.join(map(convert_to_fake_bin, number_string))


def convert_to_fake_bin(char):
    return '1' if int(char) >= 5 else '0'