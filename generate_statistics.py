import numpy as np


def project_list(file_name):
    with open(file_name, 'r', encoding="utf8") as f_in:
        li = [x.strip() for x in f_in]
    print(len(li))

    word_array = np.array(li, dtype=np.unicode_)
    char_2d_array = word_array.view('U1').reshape((word_array.size, -1))

    # print(char_2d_array)
    unique, counts = np.unique(char_2d_array[:, 0], return_counts=True)
    assert len(unique) == len(counts)
    letter_freq = dict(zip(unique, counts))
    print(''.join([f'"{k}": {v}\n' for k, v in letter_freq.items()]))


if __name__ == '__main__':
    project_list('palabras_de_cinco_letras.txt')
