import re


def get_bigrams(text):
    return [text[i:i + 2] for i in range(len(text) - 1)]


def remove_whitespace(text):
    return re.sub(r'\s+', '', text)


def remove_duplicates(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)

    return new_list
