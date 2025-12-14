data_raw = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
data = data_raw.split("\n")
num_match: dict[str, int] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def replace_first(s: str, target: str) -> str:
    try:
        i = s.index(target)
        s = s[:i] + str(num_match[target]) + s[i + len(target):]
        return s
    except ValueError:
        return s

def replace_last(s: str, target: str) -> str:
    # to be implemented
    return ""

for s in data:
    for num in num_match:
        orig = s
        s = replace_first(s, num)
        if s != orig:
            break
    for letter in s:
        if letter.isdigit():
            print(int(letter))
            break

print(replace_last("asfjsdkfjsiemvskmvsixseveneightnin", "eight"))
