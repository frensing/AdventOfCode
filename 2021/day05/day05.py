with open('input.txt', 'r') as inp:
    lines = [[list(map(int, p.split(','))) for p in line.strip().split(' -> ')] for line in inp]

field_size = [max(max(l[0][i], l[1][i]) for l in lines) + 1 for i in range(2)]
field = [[0] * field_size[0] for i in range(field_size[1])]


def compare_index(line, ind):
    return line[0][ind] == line[1][ind]


for line in lines:
    if compare_index(line, 0):
        r = sorted([line[0][1], line[1][1]])
        for i in range(r[0], r[1] + 1):
            field[i][line[0][0]] += 1

    elif compare_index(line, 1):
        r = sorted([line[0][0], line[1][0]])
        for i in range(r[0], r[1] + 1):
            field[line[0][1]][i] += 1


print("Part 1:", sum(sum(1 for x in line if x >= 2) for line in field))

for line in lines:
    if compare_index(line, 0) or compare_index(line, 1):
        continue

    x1, y1 = line[0]
    x2, y2 = line[1]

    if x1 < x2 and y1 < y2:
        for i in range(x2-x1 + 1):
            field[y1+i][x1+i] += 1

    if x1 < x2 and y1 > y2:
        for i in range(x2-x1 + 1):
            field[y1-i][x1+i] += 1

    if x1 > x2 and y1 < y2:
        for i in range(x1-x2 +1):
            field[y1+i][x1-i] += 1

    if x1 > x2 and y1 > y2:
        for i in range(x1-x2 +1):
            field[y1-i][x1-i] += 1


print("Part 2:", sum(sum(1 for x in line if x>= 2) for line in field))

