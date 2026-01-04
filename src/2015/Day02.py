from src.misc.starter_code import parse_file


def get_paper_needed(dimensions: list) -> int:
    """
    Precondition: dimensions is a sorted list
    :param dimensions: a list of dimensions of a given box
    :return: the amount of paper needed to wrap a given box
    """
    paper_needed = 0
    paper_needed += 3 * (dimensions[0] * dimensions[1])
    paper_needed += 2 * (dimensions[0] * dimensions[2])
    paper_needed += 2 * (dimensions[1] * dimensions[2])
    return paper_needed


def get_ribbon_needed(dimensions: list) -> int:
    """
    Precondition: dimensions is a sorted list
    :param dimensions: a list of dimensions of a given box
    :return: the amount of ribbon needed to wrap a given box
    """
    smallest_perimeter = 2 * (dimensions[0] + dimensions[1])
    ribbon = 1
    for side in dimensions:
        ribbon *= side
    return smallest_perimeter + ribbon


data = parse_file().split('\n')

part1_answer = 0
part2_answer = 0
for line in data:
    line = sorted([int(side) for side in line.split('x')])
    part1_answer += get_paper_needed(line)
    part2_answer += get_ribbon_needed(line)

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")