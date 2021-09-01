def contain_all_rots(keyword, words):
    if keyword == "":
        return True
    rotations = get_rotations(keyword)
    return len(rotations) == len([word for word in words if word in rotations])


def get_rotations(keyword):
    rotations = []
    for index in range(len(keyword)):
        rotations.append(f'{keyword[index:]}{keyword[:index]}')
    return rotations
 

