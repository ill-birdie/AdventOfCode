data_full = "^v^v^v^v^v"
santa_data = []
robo_data = []
for i in range(len(data_full)):
    if i % 2 == 0:
        santa_data.append(data_full[i])
    else:
        robo_data.append(data_full[i])
santa_data = "".join(santa_data)
robo_data = "".join(robo_data)

visited = set()
visited.add("[0, 0]")
def execute_directions(instructions: str) -> None:
    coord = [0, 0]
    for arrow in instructions:
        match arrow:
            case ">": coord[0] += 1
            case "<": coord[0] -= 1
            case "^": coord[1] += 1
            case "v": coord[1] -= 1
        visited.add(str(coord))

execute_directions(santa_data)
execute_directions(robo_data)
print(len(visited))
