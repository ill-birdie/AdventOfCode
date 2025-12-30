from src.misc.starter_code import parse_file

def convert(s: str) -> str:
    converted = ['"']
    special_chars = {"'", '"', '\\'}
    for letter in s:
        if letter in special_chars:
            converted.append('\\')
        converted.append(letter)
    converted.append('"')
    return ''.join(converted)

def get_memory(s: str) -> int:
    num_chars = 0
    i = 1
    while i < len(s[:-1]):
        curr_char = s[i]
        next_char = s[i + 1]
        num_chars += 1
        if curr_char == '\\':
            if next_char == 'x':
                i += 3
            else:
                i += 1
        i += 1
    return len(s) - num_chars

data = parse_file()
data = data.split('\n')

part1_answer = 0
part2_answer = 0
for line in data:
    part1_answer += get_memory(line)
    part2_answer += get_memory(convert(line))

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")