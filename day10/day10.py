numbers = []

with open('input.txt', 'r') as input:
    numbers = [int(line.strip()) for line in input]

numbers.sort()
max_val = numbers[-1] + 3

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


def get_combi_count(adapters):
    adapters.sort()
    combi_count = [1, ]
    if 1 in adapters:
        combi_count.append(1)
        if 2 in adapters:
            combi_count.append(2)
        else:
            combi_count.append(0)
    else:
        combi_count.append(0)
        if 2 in adapters:
            combi_count.append(1)
        else:
            combi_count.append(0)

    for i in range(3, adapters[-1] + 1):
        if i in adapters:
            combi_count.append(combi_count[i - 1] + combi_count[i - 2] + combi_count[i - 3])
        else:
            combi_count.append(0)

    return combi_count[-1]


print("Part 2:", get_combi_count(numbers))
