data = """4 5 3 2 1
4 3 5 2 1
2 1 3 4 5
2 3 1 4 5"""
data = data.split('\n')

def is_unsafe(line: list) -> int:
    is_decreasing = False
    if line[0] > line[1]:
        is_decreasing = True
    for i in range(len(line) - 1):
        if (line[i] > line[i + 1]) != is_decreasing or not (1 <= abs(line[i] - line[i + 1]) <= 3):
            if not is_decreasing:
                i += 1
            return i
    return -1

result = 0
for report in data:
    report = [int(n) for n in report.split(' ')]
    curr_return = is_unsafe(report)
    if curr_return != -1:
        orig = report.copy()
        report.pop(curr_return)
        print(orig, report)
        if is_unsafe(report) == -1:
            result += 1
    else:
        result += 1

print(result)