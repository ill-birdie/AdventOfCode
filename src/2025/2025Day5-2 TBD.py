data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
data = data.split("\n")
data = data[:data.index("")]

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

sorted_data = sort_data(data)
merged_data = []
i = 0
while i < len(data) - 1:
    print(sorted_data[i], sorted_data[i + 1])
    curr_range = merge_ranges(sorted_data[i], sorted_data[i + 1])
    i += 1
print(merged_data)

