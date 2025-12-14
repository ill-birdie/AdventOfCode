# Older code
data_raw = """"""
data = data_raw.split("\n")

dial_point = 50
touches_zero = 0
for turn in data:
    turn_val = int(turn[1:])
    orig_dial_point = dial_point
    if turn_val > 100:
        orig_val = turn_val
        turn_val %= 100
        touches_zero += (orig_val - turn_val) / 100

    if turn[0] == "L":
        dial_point -= turn_val
    else:
        dial_point += turn_val

    if dial_point < 0:
        dial_point += 100
        if orig_dial_point != 0:
            touches_zero += 1
    elif dial_point > 100:
        dial_point -= 100
        if orig_dial_point != 0:
            touches_zero += 1

    if dial_point == 100 or dial_point == 0:
        dial_point = 0
        touches_zero += 1
print(touches_zero)
