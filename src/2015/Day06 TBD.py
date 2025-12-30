from src.misc.starter_code import parse_file
import time
start_time = time.perf_counter()


class Solution:
    def __init__(self, mode: str):
        """
        Initializes the Solution class

        :param mode: Determines how the execute function behaves:
        'boolean' toggles each coordinate (on/off)
        'integer' increments/decrements each coordinate's brightness (int)
        Defaults to boolean if argument is neither
        """
        self._total_brightness = 0

        modes = {'boolean', 'integer'}
        self._mode = mode.lower()
        if self._mode not in modes:
            self._mode = 'boolean'

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

    @property
    def mode(self):
        return self._mode

    @property
    def total_brightness(self):
        return self._total_brightness


    def execute(self, cmd: str, s: list[int], e: list[int]) -> None:
        start_x = s[0]
        end_x = e[0]
        start_y = s[1]
        end_y = e[1]
        for x in range(start_x, end_x + 1):
            for y in range(start_y, end_y + 1):
                coord = f'[{x}, {y}]'
                if self._mode == 'boolean':
                    match cmd:
                        case 'on':
                            result = True
                        case 'off':
                            result = False
                        case 'toggle':
                            result = not self._grid[coord]
                        case _: continue
                    self._grid[coord] = result
                elif self._mode == 'integer':
                    match cmd:
                        case 'on':
                            result = 1
                        case 'off':
                            result = -1
                        case 'toggle':
                            result = 2
                        case _:
                            continue
                    self._grid[coord] += result
                    self._total_brightness += result
                    if self._total_brightness < 0:
                        self._total_brightness = 0

data = parse_file()
data = data.split('\n')
part1 = Solution('boolean')
part2 = Solution('integer')

for line in data:
    line = line.split(' ')
    coordinates = [i for i in line if ',' in i]
    start = [int(n) for n in coordinates[0].split(',')]
    end = [int(n) for n in coordinates[1].split(',')]

    if line[0] == 'toggle':
        part1.execute('toggle', start, end)
        part2.execute('toggle', start, end)
    else:
        command = line[1]
        part1.execute(command, start, end)
        part2.execute(command, start, end)

part1_answer = 0
for light in part1.grid:
    if part1.grid[light]:
        part1_answer += 1

"""part two is giving me the wrong answer for some reason. i don't know why.
i'll bugtest the next time i check in on this problem"""

print(f"""Part one answer: {part1_answer}
Part two answer: {part2.total_brightness}""")

end_time = time.perf_counter()
print(f'\nProcess took {round(end_time - start_time, 3)} seconds to finish executing')