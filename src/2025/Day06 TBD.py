from src.starter_code import parse_file
from functools import reduce
import operator

def parse_line(s: str) -> list:
    return [c for c in s.split(' ') if c != '']


def list_answer(l: list) -> int:
    op_match = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    curr_op = op_match.get(l[-1])
    nums = [int(n) for n in l[:-1]]
    return reduce(curr_op, nums)


data = parse_file().split('\n')
part1_grid = [[c] for c in parse_line(data[0])]
part2_grid = []
for line in data[1:]:
    line = parse_line(line)
    for idx, d in enumerate(line):
        part1_grid[idx].append(d)

part1_answer = 0
for line in part1_grid:
    part1_answer += list_answer(line)

print(f"""Part one answer: {part1_answer}
Part two answer: """)