from src.misc.starter_code import parse_file
import re


def has_straight(s: str) -> bool:
    """
    Checks if a string has a straight of three characters:
    ex. abc, xyz, hij

    :param s: The input string.
    :return: A boolean representing if the string contains a straight.
    """
    for idx, letter in enumerate(s[:-2]):
        if letter in 'yz':
            continue
        straight_next = next_char(letter)
        straight_last = next_char(straight_next)
        next_letter = s[idx + 1]
        last_letter = s[idx + 2]
        if straight_next == next_letter and straight_last == last_letter:
            return True
    return False


def has_invalid(s: str) -> bool:
    return bool(re.search('[iol]', s))


def has_two_pairs(s: str) -> bool:
    pairs = re.findall(r'([a-z])\1', s)
    return len(pairs) == 2


def is_valid(s: str) -> bool:
    if has_straight(s) and has_two_pairs(s) and not has_invalid(s):
        return True
    else:
        return False


def next_char(s: str) -> str:
    if s != 'z':
        char_ascii = ord(s) + 1
        char = chr(char_ascii)
        return char
    else:
        return 'a'


def increment(s: str) -> str:
    s = list(s)
    idx = -1
    while s[idx] == 'z':
        s[idx] = 'a'
        idx -= 1
    s[idx] = next_char(s[idx])
    return ''.join(s)


def next_password(s: str) -> str:
    while not is_valid(s):
        s = increment(s)
    return s


data = parse_file()
part1_answer = next_password(data)
part2_answer = next_password(increment(part1_answer))

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")
