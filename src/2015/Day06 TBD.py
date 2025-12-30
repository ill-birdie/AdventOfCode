from src.misc.starter_code import parse_file

def create_grid() -> dict[str, bool]:
    grid = {}
    for x in range(1000):
        for y in range(1000):
            l = [x, y]
            grid[str(l)] = False
    return grid

def execute(cmd: str, s: list[int], e: list[int]) -> None:
    start_x = s[0]
    end_x = s[1]
    start_y = e[0]
    end_y = e[1]
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            print(x, y)

data = parse_file()
data = data.split('\n')
lights = create_grid()

for line in data:
    line = line.split(' ')
    coordinates = [i for i in line if ',' in i]
    start = [int(n) for n in coordinates[0].split(',')]
    end = [int(n) for n in coordinates[1].split(',')]

    if line[0] == 'toggle':
        execute('toggle', start, end)
    else:
        command = line[1]
        execute(command, start, end)

part1_answer = 0
for light in lights:
    if lights[light]:
        part1_answer += 1

print(f"""Part one answer: {part1_answer}
Part two answer: """)