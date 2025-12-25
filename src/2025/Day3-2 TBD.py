from src.misc.starter_code import parse_file

data = parse_file()
data = data.split('\n')


def joltage(curr_num: str, num_digits: int) -> int:
    curr_result = []
    i = 0
    while len(curr_result) < num_digits:
        curr_window = curr_num[i:(i + 1) + (len(curr_num) - num_digits)]
        next_num = max(curr_window)
        curr_result.append(next_num)
        i = curr_num.index(next_num) + 1
    return int("".join(curr_result))


for num in data:
    print(f"{num} {joltage(num, 2)}")