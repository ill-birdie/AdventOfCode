data_raw = """"""
data_nums = data_raw.split("\n")

result = 0
for num in data_nums:
    data = []
    for digit in num:
        data.append(int(digit))
    largest = max(data[:len(data) - 1])
    data = data[data.index(largest) + 1:]
    second_largest = max(data)
    result += int(str(largest) + str(second_largest))
print(result)