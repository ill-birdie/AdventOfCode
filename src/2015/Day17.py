from src.misc.starter_code import parse_file

data = sorted(parse_file().split('\n'), key=int, reverse=True)
data = [int(n) for n in data]

result = 0
curr_depth = 1
combo_lengths = []
def eval_combos(curr_target: int, curr_containers: list) -> None:
    """
    A recursive function that finds and returns the total number of possible ways to
    add up curr_containers' (list) elements to reach curr_target (int) by
    incrementing result (int, variable in outer scope).
    """
    global result
    global curr_depth
    global combo_lengths
    for idx, container in enumerate(curr_containers, start=1):
        curr_diff = curr_target - container
        if curr_diff == 0:
            result += 1
            combo_lengths.append(curr_depth)
        elif curr_diff > 0:
            curr_depth += 1
            eval_combos(curr_diff, curr_containers[idx:])
    curr_depth -= 1


eval_combos(150, data)
min_length = min(combo_lengths)
num_min = len([d for d in combo_lengths if d == min_length])
print(f"""Part one answer: {result}
Part two answer: {num_min}""")