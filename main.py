import csv
import pickle
import re
import itertools

"""
NOTES

Needed data:
2: id
6: prefecture
7: address
8: address2

Sample of special rows:
6008028 - split into 3
6050874 - split into 2
"""


def remove_whitespace(text):
    return re.sub(r'\s+', '', text)

def get_bigrams(text):
    return [text[i:i + 2] for i in range(len(text) - 1)]

data_index = dict()

with open('KEN_ALL.CSV', encoding='shift-jis') as csvfile:
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

with open('data_index.pickle', 'wb') as f:
    pickle.dump(data_index, f, pickle.HIGHEST_PROTOCOL)
