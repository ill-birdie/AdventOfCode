from src.starter_code import parse_file
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
part2_answer = 0

accessed = []
can_remove = True
while can_remove:
    for line_idx, line in enumerate(data):
        for char_idx in range(len(line)):
            if accessible(data, line_idx, char_idx):
                part2_answer += 1
                accessed.append([line_idx, char_idx])

    if part1_answer == 0:
        part1_answer = part2_answer

    if len(accessed) > 0:
        for coord in accessed:
            l_idx = coord[0]
            c_idx = coord[1]
            data[l_idx][c_idx] = '.'
        accessed = []
    else:
        can_remove = False

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")