data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""
data = data.split('\n')

def is_safe(line: list) -> bool:
    is_decreasing = False
    if line[0] > line[1]:
        is_decreasing = True
    for i in range(len(line) - 1):
        if (line[i] > line[i + 1]) != is_decreasing or not (1 <= abs(line[i] - line[i + 1]) <= 3):
            return False
    return True

num_combos = 0
for report in data:
    report = [int(n) for n in report.split(' ')]
    if is_safe(report):
        num_combos += 1
print(num_combos)