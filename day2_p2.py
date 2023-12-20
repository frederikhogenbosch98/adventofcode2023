import re
import numpy as np

game_numbers = []
colors = ['red', 'green', 'blue']

def find_idx(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

with open("data/day2.txt", "r") as file:
    file_lines = file.readlines()
    for idx, line in enumerate(file_lines):
        line = line[8:-1].replace(':', '')
        sections = find_idx(line, ';')
        sections.insert(0, 0)
        sections.append(len(line))
        line_invalid = False
        game_digits = np.zeros((len(sections)-1, 3))

        for i in range(len(sections)-1):
            game = line[sections[i]:sections[i+1]].replace(';', '')
            digits = [0, 0, 0]
            for w in colors:
                for m in re.finditer(w, game):
                    word_idx = m.start()
                    digit = game[word_idx-3:word_idx].replace(',', '').strip()
                    if digit == '':
                        digit = 0
                    if w == 'red':
                        digits[0] = int(digit)
                    if w == 'green':
                        digits[1] = int(digit)
                    if w == 'blue':
                        digits[2] = int(digit)
            game_digits[i,:] = digits
        game_numbers.append(np.prod(np.ma.masked_equal(game_digits, 0.0, copy=False).max(axis=0)))
        
answer = sum(game_numbers)
print(f'answer: {answer}')