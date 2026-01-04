from src.misc.starter_code import parse_file
from collections import defaultdict

data = parse_file().split('\n')

stats = {}
for line in data:
    line = line.split(' ')
    name = line[0]
    nums = [int(n) for n in line if n.isdigit()]
    speed = nums[0]
    active_time = nums[1]
    resting_time = nums[2]
    stats[name] = [speed, active_time, resting_time]

positions = defaultdict(int)
points = defaultdict(int)
time = 2503
for second in range(time):
    for deer in stats:
        nums = stats[deer]
        speed = nums[0]
        active_time = nums[1]
        resting_time = nums[2]
        cycle_total = active_time + resting_time
        curr_time = (second % cycle_total) + 1
        if curr_time <= active_time:
            positions[deer] += speed
    furthest = max(positions.values())
    first_places = [deer for deer in positions if positions[deer] == furthest]
    for deer in first_places:
        points[deer] += 1

part1_answer = max(positions.values())
part2_answer = max(points.values())
print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")