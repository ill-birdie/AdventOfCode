from src.misc.starter_code import parse_file
from collections import defaultdict

data = parse_file()
data = data.split('\n')

newline_idx = data.index('')
molecule = data[newline_idx + 1]
data = data[:newline_idx]

conversions = defaultdict(list)
for line in data:
    line = line.split(' ')
    conversions[line[0]].append(line[-1])

print(conversions, molecule)