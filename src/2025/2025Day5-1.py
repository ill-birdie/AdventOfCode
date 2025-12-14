data_raw = """"""
data_newlines = data_raw.split("\n")
data_ranges = data_newlines[:data_newlines.index("")]
data_ids = data_newlines[data_newlines.index("") + 1:]

count = 0
for id in data_ids:
    id = int(id)
    for i in data_ranges:
        i = i.split("-")
        data = [int(i[0]), int(i[1])]
        if data[0] <= id <= data[1]:
            count += 1
            break
print(count)
