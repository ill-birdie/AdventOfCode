from src.misc.starter_code import parse_file

data_full = parse_file()
santa_data = []
robo_data = []
for idx, direction in enumerate(data_full):
    if idx % 2 == 0:
        santa_data.append(direction)
    else:
        robo_data.append(direction)
santa_data = "".join(santa_data)
robo_data = "".join(robo_data)


class Solution:
    def __init__(self):
        self.visited = set()
        self.visited.add("[0, 0]")

    def execute_directions(self, instructions: str) -> None:
        coord = [0, 0]
        for arrow in instructions:
            match arrow:
                case ">": coord[0] += 1
                case "<": coord[0] -= 1
                case "^": coord[1] += 1
                case "v": coord[1] -= 1
            self.visited.add(str(coord))


part_one = Solution()
part_two = Solution()
part_one.execute_directions(data_full)
part_two.execute_directions(santa_data), part_two.execute_directions(robo_data)
print(f"""Part one answer: {len(part_one.visited)}
Part two answer: {len(part_two.visited)}""")