from src.misc.starter_code import parse_file

data = parse_file()
data = data.split('\n')


def joltage(n: str, l: int) -> int:
    curr_result = []
    i = 0
    while len(curr_result) < l:
        curr_window = n[i:(i + 1) + (len(n) - l)]
        next_num = max(curr_window)
        curr_result.append(next_num)
        i = n.index(next_num) + 1
    return int("".join(curr_result))



for num in data:
    print(f"{num} {joltage(num, 12)}")