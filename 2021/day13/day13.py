with open('input.txt', 'r') as inp:
    points = []
    for line in inp:
        line = line.strip()
        if line == '':
            break
        points.append([int(x) for x in line.split(',')])

    instructions = []
    for line in inp:
        line = line.strip().split('=')
        instructions.append((line[0][-1], int(line[1])))


def print_field():
    width = max(p[0] for p in points) + 1
    height = max(p[1] for p in points) + 1
    for y in range(height):
        for x in range(width):
            print('#' if [x, y] in points else '.', end='')
        print()
    print()


for i in range(len(instructions)):
    instr = instructions[i]
    direction = 1 if instr[0] == 'y' else 0
    fold = instr[1]

    for p in points:
        if p[direction] > fold:
            p[direction] = 2 * fold - p[direction]

    if i == 0:
        print("Part 1:", len(set(str(p) for p in points)))

print_field()
