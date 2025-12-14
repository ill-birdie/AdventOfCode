data = """"""
data = [int(num) for num in data.split("\n")]

count = 0
for num in range(1, len(data)):
    if data[num] > data[num - 1]:
        count += 1
print(count)
