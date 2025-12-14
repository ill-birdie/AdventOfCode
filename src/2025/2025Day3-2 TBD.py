# Test case 11131 does not work because the first three digits should not be in the result string
data_raw = """"""
data = data_raw.split("\n")

real_sum = 0
for num in data:
    num = list(str(num))

    # the issue in question:
    result = [max(num[0:3])]
    omitted = num.index(result[0])
    idx = omitted + 1
    while omitted < 3 and idx < len(num):
        if num[idx] != min(num):
            result.append(num[idx])
        else:
            omitted += 1
        idx += 1
    result.append("".join(num[idx:]))

    # Removes any whitespace elements caused by trying to append the element after the list
    result = [num for num in result if num != ""]

    # Forces 3 elements from the number.
    while omitted < 3:
        result.remove(min(result))
    omitted += 1
result = "".join(result)
real_sum += int(result)
print(real_sum)

