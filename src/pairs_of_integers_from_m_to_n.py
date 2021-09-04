def generate_pairs(m, n):
    if type(m) != int:
        raise ValueError(f"m ({m}) provided is not a valid integer.")
    if type(n) != int:
        raise ValueError(f"m ({n}) provided is not a valid integer.")

    pairs = []
    for parent_number in range(m, n + 1, 1):
        for child_number in range(parent_number, n + 1, 1):
            pairs.append((parent_number, child_number))
    return pairs
