numbers = []

with open('input.txt', 'r') as input:
    for line in input:
        numbers.append(int(line.strip()))

numbers.sort()

prev_num = 0
jolt_1 = 0
jolt_3 = 1
for num in numbers:
    if num - prev_num == 1:
        jolt_1 += 1
    elif num - prev_num == 3:
        jolt_3 += 1
    prev_num = num

print("Part 1:", jolt_1 * jolt_3)
