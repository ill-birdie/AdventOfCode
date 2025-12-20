import time

def generate_sequence(n: int) -> list:
    """
    Generates n digits of the Recamán sequence.
    :param n: An integer representing the number of digits to generate.
    :return: A list containing n digits of the Recamán sequence.
    """
    sequence = []
    seen_nums = set()
    curr_num = 0
    for i in range(1, n + 1):
        prev_num = curr_num
        if curr_num - i > 0 and curr_num - i not in seen_nums:
            curr_num -= i
        else:
            curr_num += i
        sequence.append(prev_num)
        seen_nums.add(prev_num)
    return sequence


start_time = time.perf_counter()
print(generate_sequence(10000))
print(f"Operation took {round(time.perf_counter() - start_time, 3)} seconds")