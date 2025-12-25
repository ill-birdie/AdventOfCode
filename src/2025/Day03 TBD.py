from src.misc.starter_code import parse_file

data = parse_file()
data = data.split('\n')


def joltage(curr_num: str, num_digits: int) -> int:
    joltage_max = []
    start_idx = 0
    for i in range(num_digits):
        window_length = (len(curr_num) - num_digits) + 1
        window = curr_num[i:i + window_length]
        window = list(window)
        window = window[start_idx:]
        next_num = max(window)
        next_num_idx = curr_num.index(next_num) - i
        if next_num_idx > start_idx:
            start_idx = next_num_idx + 1
        print(start_idx)
        joltage_max.append(next_num)
    return int("".join(joltage_max))


result = 0
for jolt in data:
    curr_jolt = joltage(jolt, 12)
    print(curr_jolt)
print(result)