# wordle-es

Utilities to throw useful statistics on valid 5-letter spanish words

## process_raw_dataset.py

Processes `0_palabras_todas.txt` to create a unique 5-letter word dataset (`palabras_de_cinco_letras.txt`)

## generate_statistics.py
Output:
```
9528 words read from palabras_de_cinco_letras.txt
47640 letters in 9528 five-letter-words
The five most common letters and their percentage are:
a: 16.55%
e: 10.37%
o: 9.55%
r: 7.14%
i: 6.51%

Top words containing most common letters are:
aireo: 0.5012384550797648
seora: 0.48751049538203195
rosea: 0.48751049538203195
raseo: 0.48751049538203195
osare: 0.4875104953820319
```
