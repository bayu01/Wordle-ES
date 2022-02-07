from utils.np_utils import get_letter_weights as weight_lttr
from utils.file_utils import get_char2darray_from_file as as_char2d_array
from utils.word_utils import get_word_value as get_value
import numpy as np

if __name__ == '__main__':
    char_2d_array = as_char2d_array('palabras_de_cinco_letras.txt')
    # print(char_2d_array)
    letter_weights = weight_lttr(char_2d_array)
    entries = np.apply_along_axis(get_value, 1, char_2d_array, letter_weights)
    sorted_array = entries[np.argsort(entries[:, 1]), ]
    cumulative_stats = ''.join([f'{wrd}: {val}\n' for wrd, val in sorted_array[-5:]])
    print(f'Top words containing most common letters are:\n{cumulative_stats}')
