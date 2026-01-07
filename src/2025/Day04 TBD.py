from src.misc.starter_code import parse_file
from typing import List


def accessible(grid: List[List[str]], row: int, column: int) -> bool:
    num_neighbors = 0
    curr_char = grid[row][column]
    if curr_char == '@':
        for i in range(row - 1, row + 2):
            for j in range(column - 1, column + 2):
                within_bounds = 0 <= i < len(grid) and 0 <= j < len(grid[row])
                is_itself = (i == row and j == column)
                if within_bounds and not is_itself:
                    neighbor = grid[i][j]
                    if neighbor == '@':
                        num_neighbors += 1
        return num_neighbors < 4
    else:
        return False


data = parse_file().split('\n')
data = [list(l) for l in data]

part1_answer = 0
for line_idx, line in enumerate(data):
    for char_idx, char in enumerate(line):
        if accessible(data, line_idx, char_idx):
            part1_answer += 1

removable_data = data.copy()

print(f"""Part one answer: {part1_answer}
Part two answer: {0}""")