data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
data = data.split("\n")

num_combos = 0
for line in data:
    first_num = 0
    for letter in line:
        if letter.isdigit():
            first_num = letter
            break
    last_num = 0
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            last_num = line[i]
            break
    num_combos += int(first_num + last_num)
print(num_combos)