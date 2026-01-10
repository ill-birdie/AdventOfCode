from src.starter_code import parse_file


def bounds(r: str) -> list:
    return [int(bound) for bound in r.split('-')]


def merge_ranges(r1: str, r2: str) -> str:
    r1 = bounds(r1)
    r2 = bounds(r2)

    if r2[0] < r1[0]:
        temp = r1
        r1 = r2
        r2 = temp

    merged = []
    for bound in r2:
        if r1[0] <= bound <= r1[1]:
            merged.append(r1[len(merged)])

    merged_str = ""
    if len(merged) == 2:
        merged_str = f"{merged[0]}-{merged[1]}"
    elif len(merged) == 1:
        merged_str = f"{merged[0]}-{r2[1]}"
    return merged_str


def sort_data(range_list: list) -> list:
    data_dict = {}
    for r in range_list:
        r = bounds(r)
        data_dict[r[0]] = r[1]
    lower_bounds = sorted(data_dict.keys(), key=int)
    sorted_ranges = []
    for bound in lower_bounds:
        sorted_ranges.append(f"{bound}-{data_dict[bound]}")
    return sorted_ranges


def merge_all(range_list: list) -> list:
    range_list = sort_data(range_list)
    idx = 0
    while idx < len(range_list) - 1:
        curr_range = range_list[idx]
        next_range = range_list[idx + 1]
        curr_merged = merge_ranges(curr_range, next_range)
        if curr_merged != '':
            range_list.pop(idx)
            range_list.pop(idx)
            range_list.insert(idx, curr_merged)
        else:
            idx += 1
    return range_list


def valid_ids(range_list: list, id_list) -> int:
    num_valid = 0
    for i in id_list:
        for r in range_list:
            r = bounds(r)
            if r[0] <= i <= r[1]:
                num_valid += 1
    return num_valid


def num_fresh(range_list: list) -> int:
    fresh = 0
    for r in range_list:
        r = bounds(r)
        fresh += (r[1] - r[0]) + 1
    return fresh


data = parse_file()
data = data.split('\n')

ranges = data[:data.index("")].copy()
ranges = merge_all(ranges)

ids = data[data.index("") + 1:]
ids = [int(n) for n in ids]

part1_answer = valid_ids(ranges, ids)
part2_answer = num_fresh(ranges)

print(f"""Part one answer: {part1_answer}
Part two answer: {part2_answer}""")
