import time
start_time = time.perf_counter()

start_val = 1113222113
result = []
for digit in str(start_val):
    result.append(int(digit))

numTimes = 50
for i in range(1, numTimes + 1):
    if i >= 50:
        print(f"Processing iteration {str(i)}")
    data = result
    result = []
    changes = [0]
    for num in range(len(data) - 1):
        if data[num] != data[num + 1]:
            changes.append(num + 1)
    changes.append(len(data))
    for num in range(len(changes) - 1):
        result.append(changes[num + 1] - changes[num])
        result.append(int(data[changes[num]]))
print(len(result))

end_time = time.perf_counter()
print(f"{str(numTimes)} iterations took {str(round(end_time - start_time, 2))} seconds")
