from collections import Counter

data = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
data = data.split('\n')

num_valid = 0
for line in data:
    line = line.split(' ')
    bounds = (line[0].split('-'))
    l_bound = int(bounds[0])
    u_bound = int(bounds[1])
    target = line[1][0]
    line = line[2]

    line_count = Counter(line)
    if l_bound <= line_count[target] <= u_bound:
        num_valid += 1
print(num_valid)