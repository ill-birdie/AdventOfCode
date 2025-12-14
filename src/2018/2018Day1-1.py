data = """+1
+2
-3"""
data = data.split("\n")
result = 0
for i in data:
    match i[0]:
        case "+": result += int(i[1:])
        case "-": result -= int(i[1:])
print(result)
