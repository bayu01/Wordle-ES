import re
from unicodedata import normalize

import numpy as np


def remove_diacritics(text):
    """
    Remove diacritics from a text.
    """
    denormalized = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
        normalize("NFD", text), 0, re.I
    )
    return normalize('NFC', denormalized)


def save_list_to_file(filename, my_list):
    with open(filename, 'w', encoding='utf8') as f_out:
        for line in my_list:
            f_out.write(f'{line}\n')
    print(f'{len(my_list)} lines written to {filename}')


def get_char2darray_from_file(file_name):
    with open(file_name, 'r', encoding="utf8") as f_in:
        li = [x.strip() for x in f_in]
    print(f'{len(li)} words read from {file_name}')
    word_array = np.array(li, dtype=np.unicode_)
    char_2d_array = word_array.view('U1').reshape((word_array.size, -1))
    total_letters = char_2d_array.size
    print(f'{total_letters} letters in {len(li)} five-letter-words')
    return char_2d_array
