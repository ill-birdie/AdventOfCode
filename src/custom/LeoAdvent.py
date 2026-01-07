from src.starter_code import parse_file

def generate_sequence(n: int) -> dict[int, int]:
    """
    Generates digits of the Recamán sequence until n is reached.
    :param n: An integer representing the digit at which to stop generating the sequence.
    :return: A dictionary containing n digits of the Recamán sequence (key)
    and their last appearance (value).
    """
    seq = {}
    seen_nums = set()
    curr_num = 0
    j = 0
    while curr_num != n:
        prev_num = curr_num
        if curr_num - j > 0 and curr_num - j not in seen_nums:
            curr_num -= j
        else:
            curr_num += j
        seq[curr_num] = j
        seen_nums.add(prev_num)
        j += 1
    return seq


data = parse_file()
data = [int(n) for n in data.split('-')]

test_num = 744
sequence = generate_sequence(test_num)

curr_result = data[0]
for i in range(data[0], data[1] + 1):
    if i not in sequence:
        continue
    if sequence[i] < sequence[curr_result]:
        curr_result = i
print(f"Between {data[0]}-{data[1]}, {curr_result} appears earliest in sequence at index {sequence[curr_result]}")