import re
from unicodedata import normalize


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
