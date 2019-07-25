import pickle

from constants import INDEX_FILE_DIR
from utils import get_bigrams, remove_whitespace


def output_data(search_term=''):
    search_term = remove_whitespace(search_term)

    # Raise error for non-bigram input?
    if len(search_term) < 2:
        print('Input is not a valid bigram.')
        return

    data = None
    with open(INDEX_FILE_DIR, 'rb') as f:
        data = pickle.load(f)

    if data:
        matching_data = [data[bigram] for bigram in get_bigrams(search_term)
                                      if bigram in data]

        for bigram_matches in matching_data:
            for row in bigram_matches:
                print(','.join(['"{}"'.format(value) for value in row]))