from src.misc.starter_code import parse_file


def simulate(time: int, v: int, a_t: int, r_t: int) -> int:
    total_time = a_t + r_t
    distance = 0
    for second in range(time):
        cycle_time = (second % total_time) + 1
        if cycle_time <= a_t:
            distance += v
    return distance


data = parse_file().split('\n')

race_time = 2503
reindeer = {}
for line in data:
    line = line.split(' ')
    name = line[0]
    nums = [int(n) for n in line if n.isdigit()]
    speed = nums[0]
    active_time = nums[1]
    resting_time = nums[2]
    reindeer[name] = simulate(race_time, speed, active_time, resting_time)

part1_answer = max(reindeer.values())
print(f"""Part one answer: {part1_answer}""")