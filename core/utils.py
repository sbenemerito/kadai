import re


def get_bigrams(text):
    return [text[i:i + 2] for i in range(len(text) - 1)]


def remove_whitespace(text):
    return re.sub(r'\s+', '', text)
