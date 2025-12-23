from src.misc.starter_code import parse_file


result = 0
def get_combinations(curr_target, curr_containers):
    """
    A recursive function that finds and returns the total number of possible ways to
    add up curr_containers' (list) elements to reach curr_target (int) by
    incrementing result (int, instance variable).
    """

    global result
    for idx, container in enumerate(curr_containers):
        curr_diff = curr_target - container
        if curr_diff == 0:
            result += 1
        elif curr_diff > 0:
            get_combinations(curr_diff, curr_containers[idx + 1:])
    return result

data = sorted(parse_file().split('\n'), key=int, reverse=True)
data = [int(n) for n in data]

print(f"""Part one answer: {get_combinations(150, data)}
Part two answer: """)