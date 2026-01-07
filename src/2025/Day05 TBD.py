from src.starter_code import parse_file


def merge_ranges(r1: str, r2: str) -> str:
    r1 = [int(bound) for bound in r1.split("-")]
    r2 = [int(bound) for bound in r2.split("-")]

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


def sort_data(arr: list) -> list:
    data_dict = {}
    for r in arr:
        r = r.split('-')
        data_dict[r[0]] = r[1]
    lower_bounds = sorted(data_dict.keys(), key=int)
    sorted_arr = []
    for bound in lower_bounds:
        sorted_arr.append(f"{bound}-{data_dict[bound]}")
    return sorted_arr


data = parse_file()
data = data.split('\n')

ranges = data[:data.index("")].copy()
ranges = sort_data(ranges)
# check if merged_data returns an empty string (didn't merge anything) and increment the loop variable if so (otherwise don't)
idx = 0
while idx < len(ranges):
    curr_merged = merge_ranges(ranges[idx], ranges[idx + 1])
    if curr_merged != '':
        print('hi')

print(ranges)

ids = data[data.index("") + 1:]
ids = [int(n) for n in ids]


part1_answer = 0
for i in ids:
    for r in ranges:
        r = r.split("-")
        r = [int(n) for n in r]
        if r[0] <= i <= r[1]:
            part1_answer += 1
            break
print(f"""Part one answer: {part1_answer}
Part two answer: """)
