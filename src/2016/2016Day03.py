from src.misc.starter_code import parse_file


def valid_triangle(sides: list) -> bool:
    return sides[0] + sides[1] > sides[2]


temp_data = parse_file()
temp_data = temp_data.split('\n')
data = []

num_valid = 0
for line in temp_data:
    line = line.split(' ')
    line = [int(num) for num in line if num != '']
    line = sorted(line)
    if valid_triangle(line):
        num_valid += 1
print(num_valid)