data = """"""
data = [int(num) for num in data.split("\n")]
checked = set()
for num in data:
    needed_num = 2020 - num
    if needed_num in checked:
        print(num * needed_num)
        break
    checked.add(num)
