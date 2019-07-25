import argparse
import csv
import os
import pickle
import itertools

from constants import BASE_DIR, INDEX_FILE, INDEX_FILE_DIR
from utils import get_bigrams, remove_whitespace

CSV_FILE = 'KEN_ALL.CSV'
DEFAULT_SOURCE = os.path.join(BASE_DIR, CSV_FILE)


def generate_index_file(data_source=DEFAULT_SOURCE):
    data_index = dict()

    with open(data_source, encoding='shift-jis') as csvfile:
        print('Generating index file from data source...')
        reader = csv.reader(csvfile)

        for row in reader:
            row_id = remove_whitespace(row[2])
            row_pref = remove_whitespace(row[6])
            row_address = remove_whitespace(row[7])
            row_address2 = remove_whitespace(row[8])

            data_row = [row_id, row_pref, row_address, row_address2]

            bigrams = []
            for item in [row_pref, row_address, row_address2]:
                bigrams.append(get_bigrams(item))

            bigrams = list(dict.fromkeys(itertools.chain(*bigrams)))
            for bigram in bigrams:
                if bigram in data_index:
                    data_index[bigram].append(data_row)
                else:
                    data_index[bigram] = [data_row]

    with open(INDEX_FILE_DIR, 'wb') as f:
        pickle.dump(data_index, f, pickle.HIGHEST_PROTOCOL)

    print('Index file successfully created as {}'.format(INDEX_FILE))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generate index file for a specified data source.'
    )
    parser.add_argument('-s', '--source',
                        help='Directory of data source to be used')
    args = parser.parse_args()

    try:
        generate_index_file(data_source=args.source)
    except FileNotFoundError as e:
        print('Specified file not found, falling back to default data source.')
        generate_index_file()
