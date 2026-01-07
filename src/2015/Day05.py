import re
from src.starter_code import parse_file


def num_vowels(s: str) -> int:
    vowels = re.findall(r'[aeiou]', s)
    return len(vowels)


def contains_pair(s: str) -> bool:
    match = re.search(r'(.)\1', s)
    return bool(match)


def contains_naughty(s: str) -> bool:
    match = re.search(r"ab|cd|pq|xy", s)
    return bool(match)


def contains_sandwich(s: str) -> bool:
    match = re.search(r"(.).\1", s)
    return bool(match)


def contains_pair_twice(s: str) -> bool:
    match = re.search(r"(..).*\1", s)
    return bool(match)


def nice_part1(s: str) -> bool:
    return num_vowels(s) >= 3 and contains_pair(s) and not contains_naughty(s)

def nice_part2(s: str) -> bool:
    return contains_sandwich(s) and contains_pair_twice(s)

data = parse_file()
data = data.split('\n')

part1_result = 0
part2_result = 0
for line in data:
    if nice_part1(line):
        part1_result += 1
    if nice_part2(line):
        part2_result += 1
print(f"""Part 1 result: {part1_result}
Part 2 result: {part2_result}""")
