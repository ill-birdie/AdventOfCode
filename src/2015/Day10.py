import time
from src.misc.starter_code import parse_file
start_time = time.perf_counter()


def get_next(prev_result: list) -> list:
    """
    Outputs the next number of a given input using the look-and-say rules.
    :param prev_result: The input number (list).
    :return: The next number in the look-and-say sequence.
    """
    prev_result = [int(n) for n in prev_result]
    new_result = []

    beginnings = [0]
    for j, (prev_num, curr_num) in enumerate(zip(prev_result, prev_result[1:]), start=1):
        if curr_num != prev_num:
            beginnings.append(j)
    beginnings.append(len(prev_result))

    for prev_idx, curr_idx in zip(beginnings, beginnings[1:]):
        new_result.append(curr_idx - prev_idx)
        new_result.append(prev_result[prev_idx])
    return new_result


start_val = parse_file()
start_val = [int(n) for n in list(start_val)]

num_times = 50
for i in range(1, num_times + 1):
    if i >= 50:
        print(f"Processing iteration {str(i)}")
    start_val = get_next(start_val)
print(len(start_val))


end_time = time.perf_counter()
print(f"{str(num_times)} iterations took {str(round(end_time - start_time, 2))} seconds")
