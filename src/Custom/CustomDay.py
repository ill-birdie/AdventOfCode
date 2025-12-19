import random
import time
begin_time = time.perf_counter()

def parse_data() -> str:
    with open("C:/Users/soona/IdeaProjects/AdventOfCode/src/Custom/data.txt", "r") as data:
        parsed = data.read()
        return parsed


def generate(num_times: int) -> str:
    output = """"""
    directions = ["RIGHT", "LEFT", "UP", "DOWN", "FORWARD", "BACKWARD"]
    for i in range(num_times):
        output += f"{random.choice(directions)} {random.randint(1, 9999)}"
        if i != num_times - 1:
            output += "\n"
    return output


def get_movement(m: str) -> list:
    match m[0]:
        case "RIGHT":
            axis = 0
            direction = 1
        case "LEFT":
            axis = 0
            direction = -1
        case "UP":
            axis = 1
            direction = 1
        case "DOWN":
            axis = 1
            direction = -1
        case "FORWARD":
            axis = 2
            direction = 1
        case "BACKWARD":
            axis = 2
            direction = -1
        case _:
            axis = -1
            direction = -1
    return [axis, direction]

data = parse_data()
data = data.split("\n")

locations = {}
curr_coord = [0, 0, 0]
for move in data:
    move = move.split(" ")
    vector_components = get_movement(move)
    for num_ration in range(int(move[1])):
        curr_coord[vector_components[0]] += vector_components[1]
        if curr_coord == [0, 0, 0]:
            continue
        if str(curr_coord) not in locations.keys():
            locations[str(curr_coord)] = 1
        else:
            locations[str(curr_coord)] += 1

most_rations = max(locations.values())
result = 0
for num_ration in locations.values():
    if num_ration == most_rations:
        result += num_ration
print(result)

end_time = time.perf_counter()
print(f"Operation took {round(end_time - begin_time, 3)} seconds")
