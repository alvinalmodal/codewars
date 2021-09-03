def split(word, part_length):
    return " ".join([word[index:index + part_length] for index in range(0,len(word),part_length)])