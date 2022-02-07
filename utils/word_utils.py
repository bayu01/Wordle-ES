def get_word_value(wrd, values_dict):
    # assert type(wrd) == str
    val = 0
    for idx, c in enumerate(wrd):
        # print(f'{wrd[idx+1:len(wrd)]}')
        if c in wrd[idx + 1:len(wrd)]:
            continue
        val += values_dict.get(c)
    return ''.join(wrd), val
