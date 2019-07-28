import re


def get_bigrams(text):
    return [text[i:i + 2] for i in range(len(text) - 1)]


def get_special_bigrams(row):
    bigrams = []
    for index, pref_ch in enumerate(row[0]):
        iteration_bigrams = []
        if index < (len(row[0]) - 1):
            iteration_bigrams.append(row[0][index:index+2])
            iteration_bigrams.append(row[0][index+1::-1])

        for i, address_ch in enumerate(row[1]):
            if i < (len(row[1]) - 1):
                iteration_bigrams.append(row[1][i:i+2])
                iteration_bigrams.append(row[1][i+1::-1])

            iteration_bigrams.append('{}{}'.format(pref_ch, address_ch))
            iteration_bigrams.append('{}{}'.format(address_ch, pref_ch))

            for x, itemx in enumerate(row[2]):
                iteration_bigrams.append('{}{}'.format(address_ch, itemx))
                iteration_bigrams.append('{}{}'.format(itemx, address_ch))

        for j, address2_ch in enumerate(row[2]):
            if j < (len(row[2]) - 1):
                iteration_bigrams.append(row[2][j:j+2])
                iteration_bigrams.append(row[2][j+1::-1])

            iteration_bigrams.append('{}{}'.format(pref_ch, address2_ch))
            iteration_bigrams.append('{}{}'.format(address2_ch, pref_ch))

        bigrams.append(iteration_bigrams)

    return bigrams


def remove_whitespace(text):
    return re.sub(r'\s+', '', text)


def remove_duplicates(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)

    return new_list
