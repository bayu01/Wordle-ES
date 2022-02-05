import numpy as np


def project_list(file_name):
    with open(file_name, 'r', encoding="utf8") as f_in:
        li = [x.strip() for x in f_in]
    print(len(li))

    word_array = np.array(li, dtype=np.unicode_)
    char_2d_array = word_array.view('U1').reshape((word_array.size, -1))

    # print(char_2d_array)
    unique, counts = np.unique(char_2d_array, return_counts=True)
    assert len(unique) == len(counts)
    letter_freq = dict(zip(unique, counts))
    print(''.join([f'"{k}": {v}\n' for k, v in letter_freq.items()]))

    total_letters = char_2d_array.size
    print(f'total letters {total_letters}')

    letters_wt_values = dict(map(lambda kv: (kv[0], kv[1]/total_letters), letter_freq.items()))
    print(''.join([f'"{k}": {v}\n' for k, v in letters_wt_values.items()]))


if __name__ == '__main__':
    project_list('palabras_de_cinco_letras.txt')
