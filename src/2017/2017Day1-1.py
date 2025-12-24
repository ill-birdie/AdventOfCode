data = ""
valid_nums = []
for digit in range(len(data) - 1):
    if data[digit] == data[digit + 1]:
        valid_nums.append(int(data[digit]))
if data[-1] == data[0]:
    valid_nums.append(int(data[-1]))
    
num_combos = 0
for digit in valid_nums:
    num_combos += digit
print(num_combos)
