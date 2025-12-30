from src.misc.starter_code import parse_file
import time
start_time = time.perf_counter()


class Solution:
    def __init__(self):
        self._grid = {}
        for x in range(1000):
            for y in range(1000):
                l = [x, y]
                self._grid[str(l)] = False

    def __getitem__(self, coord):
        return self._grid[coord]

    @property
    def grid(self):
        return self._grid


    def execute(self, cmd: str, s: list[int], e: list[int]) -> None:
        start_x = s[0]
        end_x = e[0]
        start_y = s[1]
        end_y = e[1]
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                coord = f'[{x}, {y}]'
                result: bool
                match cmd:
                    case 'on': result = True
                    case 'off': result = False
                    case 'toggle': result = not self._grid[coord]
                    case _: continue
                self._grid[coord] = result

data = parse_file()
data = data.split('\n')
foo = Solution()

for line in data:
    line = line.split(' ')
    coordinates = [i for i in line if ',' in i]
    start = [int(n) for n in coordinates[0].split(',')]
    end = [int(n) for n in coordinates[1].split(',')]

    if line[0] == 'toggle':
        foo.execute('toggle', start, end)
    else:
        command = line[1]
        foo.execute(command, start, end)

part1_answer = 0
for light in foo.grid:
    if foo.grid[light]:
        part1_answer += 1

print(f"""Part one answer: {part1_answer}
Part two answer: """)

end_time = time.perf_counter()
print(f'Program took {round(end_time - start_time, 3)} seconds to finish executing')