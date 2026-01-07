from src.starter_code import parse_file


def valid_triangle(sides: list) -> bool:
    """
    Tests if a triangle is valid.
    :param sides: A list containing three sides of a triangle.
    :return: Returns a boolean representing if the sides form a valid triangle.
    """
    sides = sorted(sides, key=int, reverse=False)
    return sides[0] + sides[1] > sides[2]


def get_part1(d: str) -> int:
    d = d.split('\n')
    num_valid1 = 0
    for sides in d:
        sides = sides.split(' ')
        sides = [int(side) for side in sides if side != '']
        if valid_triangle(sides):
            num_valid1 += 1
    return num_valid1


def get_part2(unparsed: str) -> int:
    unparsed = unparsed.split('\n')
    unparsed = ' '.join(unparsed).split(' ')
    unparsed = [side for side in unparsed if side != '']
    unparsed = [int(side) for side in unparsed]
    parsed = []
    for side1, side2, side3 in zip(unparsed, unparsed[3:], unparsed[6:]):
        parsed.append([side1, side2, side3])

    num_valid2 = 0
    for sides in parsed:
        if valid_triangle(sides):
            num_valid2 += 1
    return num_valid2


temp_data = parse_file()
print(f"""Part one answer: {get_part1(temp_data)}
Part two answer: {get_part2(temp_data)}""")