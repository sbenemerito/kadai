import argparse
import pickle

from core.constants import INDEX_FILE_DIR
from core.indexer import generate_index_file
from core.searcher import query_data


def generate_index(data_source=None):
    try:
        if data_source is None:
            generate_index_file()
        else:
            generate_index_file(data_source=data_source)
    except FileNotFoundError as e:
        print('Data source not found!')


def search():
    data = None
    with open(INDEX_FILE_DIR, 'rb') as f:
        data = pickle.load(f)

    while True:
        query = input('入力：')

        if query == '':
            break

        print('出力')
        results = query_data(search_term=query, data=data)
        for row in results:
            print(','.join(['"{}"'.format(value) for value in row]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='二次面接課題'
    )
    subparsers = parser.add_subparsers(dest='subparser')

    indexer_parser = subparsers.add_parser('generate_index')
    indexer_parser.add_argument(
        '-s', '--source',
        dest='data_source',
        help='directory of data source to be used'
    )

    searcher_parser = subparsers.add_parser('search')

    kwargs = vars(parser.parse_args())
    globals()[kwargs.pop('subparser')](**kwargs)
