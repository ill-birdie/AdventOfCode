data = "R5, L5, R5, R3"
data = data.split(", ")

degrees = 0
coord = [0, 0]
for move in data:
    match move[0]:
        case "R": degrees += 90
        case "L": degrees -= 90

    magnitude = int(move[1:])
    match degrees % 360:
        case 0: coord[1] += magnitude
        case 180: coord[1] -= magnitude
        case 90: coord[0] += magnitude
        case 270: coord[0] -= magnitude
print(abs(coord[0]) + abs(coord[1]))
