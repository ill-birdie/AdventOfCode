data = "R1, R1, R1, R1"
data = data.split(", ")

locations = set()
curr_coord = [0, 0]
degrees = 0
found = False
for move in data:
    if found:
        break

    match move[0]:
        case "R": degrees += 90
        case "L": degrees -= 90

    match degrees % 360:
        case 0:
            axis = 1
            direction = 1
        case 180:
            axis = 1
            direction = -1
        case 90:
            axis = 0
            direction = 1
        case 270:
            axis = 0
            direction = -1

    for i in range(int(move[1])):
        curr_coord[axis] += direction
        if str(curr_coord) not in locations:
            locations.add(str(curr_coord))
        else:
            found = True
            break

print(locations)
if found:
    print(abs(curr_coord[0]) + abs(curr_coord[1]))
else:
    print("Not found")