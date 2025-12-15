data_raw = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
data = data_raw.split("\n")
num_match = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def find_first(s: str) -> str:
    for i in range(len(s)):
        if s[i].isdigit():
            return s[i]
        for num in num_match:
            if num in s[:i + 1]:
                return num_match[num]
    return ""

def find_last(s: str) -> str:
    for i in range(len(s) - 1, -1, -1):
        if s[i].isdigit():
            return s[i]
        for num in num_match:
            if num in s[i:]:
                return num_match[num]
    return ""

result = 0
for line in data:
    result += int(find_first(line) + find_last(line))
print(result)