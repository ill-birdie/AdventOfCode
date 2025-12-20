import re
from src.misc.starter_code import parse_file


data = parse_file()
data = data.split('\n')


def parse_match(m) -> bool:
    if m is None:
        return False
    else:
        return True


def is_vowel(s: str) -> bool:
    match = re.search(r"[aeiou]", s)
    return bool(match)


def num_vowels(s: str) -> int:
    count = 0
    for letter in s:
        if is_vowel(letter):
            count += 1
    return count


def contains_double(s: str) -> bool:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return True
    return False


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
    if num_vowels(s) >= 3 and contains_double(s) and not contains_naughty(s):
        return True
    else:
        return False


def nice_part2(s: str) -> bool:
    if contains_sandwich(s) and contains_pair_twice(s):
        return True
    else:
        return False


part1_result = 0
part2_result = 0
for line in data:
    if nice_part1(line):
        part1_result += 1
    if nice_part2(line):
        part2_result += 1
print(f"""Part 1 result: {part1_result}
Part 2 result: {part2_result}""")
