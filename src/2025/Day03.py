from src.starter_code import parse_file

data = parse_file()
data = data.split('\n')


def get_joltage(curr_num: str, num_digits: int) -> int:
    """
    Need to define an end index. The starting index works fine.
    The end index should decrease if the starting index jumps.
    :param curr_num:
    :param num_digits:
    :return:
    """
    max_joltage = ''
    window_length = (len(curr_num) - num_digits) + 1
    end_idx = window_length
    for i in range(num_digits):
        window = curr_num[:end_idx]
        next_num = max(window)
        num_idx = window.index(next_num)
        curr_num = curr_num[num_idx + 1:]
        if num_idx > 0:
            end_idx -= num_idx
        max_joltage += next_num
    return int("".join(max_joltage))


part1_answer = 0
part2_answer = 0
for joltage in data:
    part1_jolt = get_joltage(joltage, 2)
    part1_answer += part1_jolt
    part2_jolt = get_joltage(joltage, 12)
    part2_answer += part2_jolt

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")