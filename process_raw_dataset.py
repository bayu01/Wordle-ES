from utils import remove_diacritics as remove_diacritics


def get_list_of_len_five_words(file_name):
    """
    process line by line of file `0_palabras_todas.txt`
    :return a list of 5 letter words with diacritics removed. There is a potential for duplicates.
    """
    five_letter_bucket = []
    with open(file_name, 'r', encoding="utf8") as f_in:
        for line in f_in:
            stripped_word = line.strip()
            if len(stripped_word) != 5:
                continue
            base_word = remove_diacritics(stripped_word)
            if not base_word.isalpha():
                continue
            base_word = base_word.lower()
            print(base_word)
            five_letter_bucket.append(base_word)
    unique = list(set(five_letter_bucket))
    print(f'{len(unique)} valid 5-letter words in dictionary')
    unique.sort()
    return unique


def save_list_to_file(filename, my_list):
    with open(filename, 'w', encoding='utf8') as f_out:
        for line in my_list:
            f_out.write(f'{line}\n')
    print(f'{len(my_list)} lines written to file')


if __name__ == '__main__':
    """
    generates a dataset ('palabras_de_cinco_letras.txt') with unique valid 5-letter spanish dictionary words
    """
    five_len_bucket = get_list_of_len_five_words('0_palabras_todas.txt')
    print(f'{len(five_len_bucket)} unique 5-letter words')
    save_list_to_file('palabras_de_cinco_letras.txt', five_len_bucket)
