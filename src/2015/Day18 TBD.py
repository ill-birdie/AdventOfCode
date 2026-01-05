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
    after_step = []
    for line in range(len(grid)):
        new_line = []
        for coord, char in enumerate(grid):
            if activated(grid, line, coord):
                new_line.append('#')
            else:
                new_line.append('.')
        after_step.append(new_line)
    return after_step


data = parse_file()
data = data.split('\n')
data = [list(line) for line in data]

result = data.copy()
for steps in range(100):
    result = simulate_step(result)
part1_answer = num_lights(result)

print(f"""Part one answer: {part1_answer}
Part two answer: """)