data = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"
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

    for i in range(int(move[1:])):
        curr_coord[axis] += direction
        if str(curr_coord) not in locations:
            locations.add(str(curr_coord))
        else:
            found = True
            break

if found:
    print(abs(curr_coord[0]) + abs(curr_coord[1]))
else:
    print("Not found")