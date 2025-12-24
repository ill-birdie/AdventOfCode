data = """"""
data = [int(i) for i in data.split("\n")]

num_combos = 0
for mass in data:
    curr_result = ((mass // 3) - 2)
    num_combos += curr_result
print(num_combos)
