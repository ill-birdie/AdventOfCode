from src.misc.starter_code import parse_file

data = parse_file()
data = data.split('\n')

def is_unsafe(line: list) -> int:
    """
    Determines if a line of data is unsafe.

    :param line: A line of data (list).
    :return: Returns the index of the point which the line becomes unsafe.
    If the data is determined to be safe, -1 is returned.
    """
    is_decreasing = False
    if line[0] > line[1]:
        is_decreasing = True
    for i in range(len(line) - 1):
        if (line[i] > line[i + 1]) != is_decreasing or not (1 <= abs(line[i] - line[i + 1]) <= 3):
            return i
    return -1

result = 0
for report in data:
    report = [int(n) for n in report.split(' ')]
    curr_return = is_unsafe(report)
    if curr_return == -1:
        result += 1
    else:
        for i in range(2):
            report_temp = report.copy()
            report_temp.pop(curr_return + i)
            if is_unsafe(report_temp) == -1:
                result += 1
                break
print(result)