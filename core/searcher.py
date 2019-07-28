import pickle

from .constants import INDEX_FILE_DIR
from .utils import get_bigrams, remove_whitespace, remove_duplicates


def query_data(search_term='', index_dir=INDEX_FILE_DIR, data=None):
    search_term = remove_whitespace(search_term)

    if data is None:
        try:
            with open(index_dir, 'rb') as f:
                data = pickle.load(f)
        except FileNotFoundError:
            print('No index file yet!')
            return []

    matching_data = []
    for bigram in get_bigrams(search_term):
        if bigram in data:
            for item in data[bigram]:
                matching_data.append(item)

    return remove_duplicates(matching_data)
