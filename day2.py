import re

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

        for i in range(len(sections)-1):
            game = line[sections[i]:sections[i+1]].replace(';', '')
            print(game)
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

            if digits[0] < 13 and digits[1] < 14 and digits[2] < 15 and not line_invalid:
                line_invalid = False
            else:
                line_invalid = True
        if not line_invalid:
            game_numbers.append(idx+1)

answer = sum(game_numbers)
print(f'answer: {answer}')