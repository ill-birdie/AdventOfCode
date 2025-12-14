data = "^v^v^v^v^v"
coord = [0, 0]
visited = set()
visited.add(str(coord))
for arrow in data:
    match arrow:
        case ">": coord[0] += 1
        case "<": coord[0] -= 1
        case "^": coord[1] += 1
        case "v": coord[1] -= 1
    visited.add(str(coord))
print(len(visited))
