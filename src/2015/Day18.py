from src.misc.starter_code import parse_file
from typing import List


def activated(grid: List[List[str]], row: int, column: int) -> bool:
    num_neighbors = 0
    curr_char = grid[row][column]
    for i in range(row - 1, row + 2):
        for j in range(column - 1, column + 2):
            within_bounds = 0 <= i < len(grid) and 0 <= j < len(grid[row])
            is_itself = (i == row and j == column)
            if within_bounds and not is_itself:
                neighbor = grid[i][j]
                if neighbor == '#':
                    num_neighbors += 1
    match curr_char:
        case '#': return num_neighbors in range(2, 4)
        case _: return num_neighbors == 3


def num_lights(grid: List[List[str]]) -> int:
    count = 0
    for row in grid:
        for c in row:
            if c == '#':
                count += 1
    return count


def simulate_step(grid: List[List[str]]) -> List[List[str]]:
    new_grid = []
    for line in range(len(grid)):
        new_line = []
        for coord, char in enumerate(grid):
            if activated(grid, line, coord):
                new_line.append('#')
            else:
                new_line.append('.')
        new_grid.append(new_line)
    return new_grid


def activate_corners(grid: List[List[str]]) -> List[List[str]]:
    new_grid = grid
    corners = [[0, 0], [-1, 0], [0, -1], [-1, -1]]
    for c in corners:
        row = c[0]
        column = c[1]
        new_grid[row][column] = '#'
    return new_grid


data = parse_file()
data = data.split('\n')
data = [list(line) for line in data]

part1_grid = data.copy()
part2_grid = activate_corners(data.copy())

for steps in range(100):
    part1_grid = simulate_step(part1_grid)
    part2_grid = activate_corners(simulate_step(part2_grid))
part1_answer = num_lights(part1_grid)
part2_answer = num_lights(part2_grid)

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")