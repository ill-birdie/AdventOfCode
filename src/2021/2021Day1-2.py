data = """"""
data = [int(num) for num in data.split("\n")]

count = 0
for num in range(3, len(data)):
    window = data[num - 1] + data[num - 2]
    curr_window = window + data[num]
    prev_window = window + data[num - 3]
    if curr_window > prev_window:
        count += 1
print(count)
