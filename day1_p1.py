cal_values = []

with open("data/day1.txt", "r") as file:
        file_lines = file.readlines()
        for line in file_lines:
            digits = (list(filter(str.isdigit, line)))
            z = int(str(digits[0]) + str(digits[-1]))
            cal_values.append(z)

print(sum(cal_values))