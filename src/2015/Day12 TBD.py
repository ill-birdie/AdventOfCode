from src.misc.starter_code import parse_file

data = parse_file()

part1_answer = 0
curr_num = ''
in_object = False
for char in data:
    if char == '{':
        in_object = True
    elif char.isdigit() or char == '-':
        curr_num += char
    elif len(curr_num) != 0:
        part1_answer += int(curr_num)
        curr_num = ''

print(f"""Part one answer: {part1_answer}
Part two answer: """)