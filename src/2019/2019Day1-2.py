data = """"""
data = [int(i) for i in data.split("\n")]
result = 0
for mass in data:
    while mass > 0:
        mass = (mass // 3) - 2
        if mass > 0:
            result += mass
print(result)