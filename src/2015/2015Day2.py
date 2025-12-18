data = """2x3x4"""
data = data.split('\n')


def get_paper_needed(dimensions: list) -> int:
    """
    Precondition: dimensions is a sorted list
    :param dimensions: a list of dimensions of a given box
    :return: the amount of paper needed to wrap a given box
    """
    paper_needed = 0
    for i in range(len(dimensions)):
        for j in range(i + 1, len(dimensions)):
            multi = 2
            # Smallest side
            if i == 0 and j == 1:
                multi = 3
            paper_needed += multi * (dimensions[i] * dimensions[j])
    return paper_needed


def get_ribbon_needed(dimensions: list) -> int:
    """
    Precondition: dimensions is a sorted list
    :param dimensions: a list of dimensions of a given box
    :return: the amount of ribbon needed to wrap a given box
    """
    smallest_perimeter = (dimensions[0] * 2) + (dimensions[1] * 2)
    bow = 1
    for side in dimensions:
        bow *= side
    return smallest_perimeter + bow


paper_amount = 0
ribbon_amount = 0
for line in data:
    line = sorted([int(side) for side in line.split('x')])
    paper_amount += get_paper_needed(line)
    ribbon_amount += get_ribbon_needed(line)
print(f"""Total square feet of wrapping paper: {paper_amount}
Total feet of ribbon: {ribbon_amount}""")