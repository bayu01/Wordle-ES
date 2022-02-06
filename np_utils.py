import numpy as np


def get_letter_weights(char_2d_array):
    unique, counts = np.unique(char_2d_array, return_counts=True)
    assert len(unique) == len(counts)
    letter_freq = dict(zip(unique, counts))
    # print(''.join([f'"{k}": {v}\n' for k, v in letter_freq.items()]))
    total_letters = char_2d_array.size
    letters_wt_values = dict(map(lambda kv: (kv[0], kv[1] / total_letters), letter_freq.items()))
    # print(''.join([f'"{k}": {v}\n' for k, v in letters_wt_values.items()]))
    sorted_lttrs = sorted(letters_wt_values.items(), key=lambda e: e[1], reverse=True)
    five_lttr_stats = ''.join([f'{k}: {100 * v:.2f}%\n' for k, v in sorted_lttrs[0:5]])
    print(f'The five most common letters and their percentage are:\n{five_lttr_stats}')
    return sorted_lttrs
