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

    operation_list = []
    oper = ''
    for col_idx in range(longest_len + 1):
        num = ''
        for row_idx, row in enumerate(grid[:-1]):
            if col_idx < len(row):
                num += row[col_idx]
            else:
                num += ' '
        if col_idx < len(grid[-1]):
            potential_oper = grid[-1][col_idx]
            if potential_oper != ' ':
                oper = potential_oper
        num = num.strip()
        if num.isdigit():
            operation_list.append(num)
        else:
            operation_list.append(oper)
            new_grid.append(operation_list)
            operation_list = []
    return new_grid

data = parse_file().split('\n')
part1_grid = init_grid1(data)
part2_grid = init_grid2(data)

part1_answer = 0
part2_answer = 0
for part1_line, part2_line in zip(part1_grid, part2_grid):
    part1_answer += list_answer(part1_line)
    part2_answer += list_answer(part2_line)

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")