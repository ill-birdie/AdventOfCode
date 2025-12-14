data = """"""
data = [int(num) for num in data.split("\n")]

data = [num for num in data if 2020 - (2 * min(data)) > num]
for i in range(len(data)):
    needed_sum = 2020 - data[i]
    checked = set()
    for j in range(i, len(data)):
        complement = needed_sum - data[j]
        if complement in checked:
            print(complement * data[i] * data[j])
        checked.add(data[j])