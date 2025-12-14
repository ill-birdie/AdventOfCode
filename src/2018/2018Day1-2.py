data_raw = """+3
+3
+4
-2
-4"""
data = data_raw.split("\n")

curr_pos = 0
seen = set()
seen.add(curr_pos)
found = False
while not found:
    for i in data:
        match i[0]:
            case "+": curr_pos += int(i[1:])
            case "-": curr_pos -= int(i[1:])

        if curr_pos not in seen:
            seen.add(curr_pos)
        else:
            print(curr_pos)
            found = True
            break
