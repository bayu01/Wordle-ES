import numpy as np
from scipy import stats as stats


def project_list(file_name):
    li = []
    with open(file_name, 'r', encoding="utf8") as f_in:
        li = [x.strip() for x in f_in]
    print(len(li))

    word_array = np.array(li, dtype=np.unicode_ )
    char_2d_array = word_array.view('U1').reshape((word_array.size, -1))

    print(char_2d_array)

    print(stats.mode(char_2d_array))


if __name__ == '__main__':
    project_list('palabras_de_cinco_letras.txt')
