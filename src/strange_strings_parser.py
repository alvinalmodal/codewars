import re


def word_splitter(sentence):
    special_chars = re.findall(r'[@_!#$%^&*()<>?/\|}{~\:;\+\=\,]', sentence)
    unique_special_chars = []
    for special_char in special_chars:
        if special_char not in unique_special_chars:
            unique_special_chars.append(special_char)

    updated_sentence = sentence[:]
    for char in unique_special_chars:
        updated_sentence = updated_sentence.replace(char,'\t')

    return [value for value in updated_sentence.split("\t") if len(value) > 0]
        
