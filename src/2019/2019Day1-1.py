data = """"""
data = [int(i) for i in data.split("\n")]

result = 0
for mass in data:
    curr_result = ((mass // 3) - 2)
    result += curr_result
print(result)
