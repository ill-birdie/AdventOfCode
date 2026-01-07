from src.starter_code import parse_file

data = parse_file()
data = data.split('\n')

part1_answer = 0
part2_answer = -1
for i, curr_num in enumerate(data[:-1]):
    next_num = data[i + 1]
    next_target = next_num[(i + 1) % len(next_num)]
    curr_target = curr_num[i % len(curr_num)]
    if curr_target == next_target:
        if part2_answer == -1:
            part2_answer = i + 1
        part1_answer += 1
print(f"""Part 1 answer: {part1_answer}
Part 2 answer: {part2_answer}
Part 3 answer: {str(part1_answer) + str(part2_answer)}""")