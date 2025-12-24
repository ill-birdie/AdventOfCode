data = """+1
+2
-3"""
data = data.split("\n")
num_combos = 0
for i in data:
    match i[0]:
        case "+": num_combos += int(i[1:])
        case "-": num_combos -= int(i[1:])
print(num_combos)
