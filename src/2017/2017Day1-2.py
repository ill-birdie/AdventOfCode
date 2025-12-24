data = ""
data_cloned = data * 2
valid_nums = []
for digit in range(len(data)):
    if data[digit] == data_cloned[digit + (len(data) // 2)]:
        valid_nums.append(int(data[digit]))

num_combos = 0
for num in valid_nums:
    num_combos += num
print(num_combos)