import re
from src.misc.starter_code import parse_file

data_ranges = parse_file().split(',')
data = []

for i in data_ranges:
    bounds = i.split("-")
    lower_bound = int(bounds[0])
    upper_bound = int(bounds[1])
    for num in range(lower_bound, upper_bound + 1):
        data.append(str(num))


def part1_invalid(n: str) -> bool:
    match = re.search(r"^(.*)\1$", n)
    return bool(match)


def part2_invalid(n: str) -> bool:
    match = re.search(r"^(.*)\1+$", n)
    return bool(match)


part1_result = 0
part2_result = 0
for num in data:
    if part1_invalid(num):
        part1_result += int(num)
    if part2_invalid(num):
        part2_result += int(num)
print(f"""Part 1 result: {part1_result}
Part 2 result: {part2_result}""")
