with open('input.txt', 'r') as inp:
    instructions = [(inst[0][0], int(inst[1])) for inst in [line.strip().split() for line in inp]]

forward = sum(inst[1] for inst in instructions if inst[0] == 'f')
depth = sum(inst[1] if inst[0] == 'd' else -inst[1] for inst in instructions if inst[0] in 'du')

print("Part 1:", forward * depth)

aim = horizontal = depth = 0
for inst in instructions:
    if inst[0] in 'du':
        aim += inst[1] if inst[0] == 'd' else -inst[1]
    else:
        horizontal += inst[1]
        depth += aim * inst[1]

print("Part 2:", horizontal * depth)
