import re

cal_values = []
number_str = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open("data/day1.txt", "r") as file:
        file_lines = file.readlines()
        for line in file_lines:
            print(line)

            digits = [int(x) for i, x in enumerate(line) if x.isdigit()]
            digits_idx = [i for i, x in enumerate(line) if x.isdigit()]

            idx_words = []
            idxs = []
            for idx, w in enumerate(number_str):
                for m in re.finditer(w, line):
                    idx_words.append(m.start())
                    idxs.append(idx+1)

            if len(idxs) != 0:
                idxs.extend(digits)
                idx_words.extend(digits_idx)
                
                full_digits, full_indices  = (list(t) for t in zip(*sorted(zip(idx_words, idxs))))
            else:
                full_digits, full_indices  = (list(t) for t in zip(*sorted(zip(digits_idx, digits))))


            # print(full_digits)
            print(full_indices)
            z = int(str(full_indices[0]) + str(full_indices[-1]))
            print(z)
            print("")

            cal_values.append(z)

print(sum(cal_values))