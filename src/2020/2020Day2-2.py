data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
data = data.split('\n')

num_valid = 0
for line in data:
    line = line.split(' ')
    positions = [int(pos) - 1 for pos in line[0].split('-')]
    target = line[1][0]
    line = line[2]

    num_found = 0
    for pos in positions:
        if line[pos] == target:
            num_found += 1
    if num_found == 1:
        num_valid += 1
print(num_valid)