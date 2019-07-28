import csv
import os
import pickle
import itertools

from .constants import BASE_DIR, INDEX_FILE_DIR
from .utils import get_special_bigrams, remove_whitespace

CSV_FILE = 'KEN_ALL.CSV'
DEFAULT_SOURCE = os.path.join(BASE_DIR, CSV_FILE)


def write_data_by_bigram(data_row=None, data_index=None):
    bigrams = get_special_bigrams(data_row[1:])

    if data_index is not None:
        bigrams = list(dict.fromkeys(itertools.chain(*bigrams)))
        for bigram in bigrams:
            if bigram in data_index:
                data_index[bigram].append(data_row)
            else:
                data_index[bigram] = [data_row]


def generate_index_file(data_source=DEFAULT_SOURCE, index_dir=INDEX_FILE_DIR):
    data_index = dict()

    with open(data_source, encoding='shift-jis') as csvfile:
        print('Generating index file from data source...')
        reader = csv.reader(csvfile)
        active_row = [None]

        for row in reader:
            zipcode = remove_whitespace(row[2]).zfill(7)
            prefecture = remove_whitespace(row[6])
            address1 = remove_whitespace(row[7])
            address2 = remove_whitespace(row[8])
            data_row = [zipcode, prefecture, address1, address2]

            if active_row[0] is None:
                active_row = data_row
                continue

            if zipcode == active_row[0]:
                active_row[3] = '{}{}'.format(active_row[3], address2)
                continue

            write_data_by_bigram(active_row, data_index)
            active_row = data_row

        # Write one more time for last active_row
        write_data_by_bigram(active_row, data_index)

    with open(index_dir, 'wb') as f:
        pickle.dump(data_index, f, pickle.HIGHEST_PROTOCOL)

    print('Index file successfully created')
