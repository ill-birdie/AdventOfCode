from src.starter_code import parse_file
from typing import List
from functools import reduce
import operator


def line_nums(s: str) -> list:
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


def init_grid1(grid: list) -> List[List[int]]:
    new_grid = [[c] for c in line_nums(grid[0])]
    for l in grid[1:]:
        l = line_nums(l)
        for idx, d in enumerate(l):
            new_grid[idx].append(d)
    return new_grid


def init_grid2(grid: list) -> List[List[int]]:
    new_grid = []
    longest_len = 0
    curr_len = len(grid[0])
    for l in grid[1:]:
        if curr_len > longest_len:
            longest_len = curr_len
        curr_len = len(l)

    """
    Iterate through each column of the list longest_len times.
    Each column joined will be a number.
    Have a list to store the current operation.
    Have a string to store the current number (column).
    If the bottom row is an operation, append the list to the grid.
    Otherwise, append the current number to the operation list.
    
    This should separate each operation based on if there's a new operation in the bottom row.
    """


data = parse_file().split('\n')
part1_grid = init_grid1(data)
part2_grid = init_grid2(data)

part1_answer = 0
for line in part1_grid:
    part1_answer += list_answer(line)

print(f"""Part one answer: {part1_answer}
Part two answer: """)