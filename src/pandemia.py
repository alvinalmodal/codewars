def infected(map):
    continents = map.split('X')

    infected = 0
    not_infected = 0
    for continent in continents:
        count = len(continent)
        if continent != '' and '1' in continent:
            infected += count
        elif continent != '' and '1' not in continent:
            not_infected += count
            
    total = infected + not_infected
    if total == 0:
        return 0
    percentage = 100 * (infected / total)
    return percentage