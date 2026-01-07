from src.starter_code import parse_file


def part1_answer() -> int:
    coord = [0, 0]
    for line in data:
        line = line.split(' ')
        magnitude = int(line[1])
        match line[0]:
            case "forward":
                coord[0] += magnitude
            case "down":
                coord[1] += magnitude
            case "up":
                coord[1] -= magnitude
    return coord[0] * coord[1]


def part2_answer() -> int:
    coord = [0, 0]
    aim = 0
    for line in data:
        line = line.split(' ')
        magnitude = int(line[1])
        match line[0]:
            case "down":
                aim += magnitude
            case "up":
                aim -= magnitude
            case "forward":
                coord[0] += magnitude
                coord[1] += (magnitude * aim)
    return coord[0] * coord[1]



data = parse_file()
data = data.split('\n')

print(f"""Part 1 answer: {part1_answer()}
Part 2 answer: {part2_answer()}""")