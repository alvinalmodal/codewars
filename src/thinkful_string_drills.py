def quotable(name, quote):
    if type(name) != str or type(quote) != str:
        raise ValueError("Please provide a valid string for name/quote.")
    return f'{name} said: "{quote}"'