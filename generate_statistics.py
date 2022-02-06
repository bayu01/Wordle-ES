from np_utils import get_letter_weights as weight_lttr
from utils import get_char2darray_from_file as as_char2d_array



if __name__ == '__main__':
    char_2d_array = as_char2d_array('palabras_de_cinco_letras.txt')
    # print(char_2d_array)
    letter_weights = weight_lttr(char_2d_array)

