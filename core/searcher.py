import pickle

from .constants import INDEX_FILE_DIR
from .utils import get_bigrams, remove_whitespace, remove_duplicates


def query_data(search_term='', index_dir=INDEX_FILE_DIR):
    search_term = remove_whitespace(search_term)

    data = None
    with open(index_dir, 'rb') as f:
        data = pickle.load(f)

    if data:
        """
        The following list comprehension is the same as this code block:
        # matching_data = []
        # for bigram in get_bigrams(search_term):
        #     if bigram in data:
        #         for item in data[bigram]:
        #             matching_data.append(item)
        """
        matching_data = [
            item for bigram in get_bigrams(search_term)
                 for item in data[bigram] if bigram in data
        ]

        return remove_duplicates(matching_data)

    return []
