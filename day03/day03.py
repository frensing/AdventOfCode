with open('day03_input.txt', 'r') as input:
    lines = [line.strip() for line in input]

hits_1 = 0
hits_2 = 0
hits_3 = 0
hits_4 = 0
hits_5 = 0

pos_x_1 = 0  # Slope 3,1
pos_x_2 = 0  # Slope 1,1
pos_x_3 = 0  # Slope 5,1
pos_x_4 = 0  # Slope 7,1
pos_x_5 = 0  # Slope 1,2
pos_y_5 = 0

for line in lines:
    if line[pos_x_1] == '#':
        hits_1 += 1
    if line[pos_x_2] == '#':
        hits_2 += 1
    if line[pos_x_3] == '#':
        hits_3 += 1
    if line[pos_x_4] == '#':
        hits_4 += 1
    if line[pos_x_5] == '#' and pos_y_5 == 0:
        hits_5 += 1

    pos_x_1 = (pos_x_1 + 3) % len(line)
    pos_x_2 = (pos_x_2 + 1) % len(line)
    pos_x_3 = (pos_x_3 + 5) % len(line)
    pos_x_4 = (pos_x_4 + 7) % len(line)
    if pos_y_5 == 0:
        pos_x_5 = (pos_x_5 + 1) % len(line)
    pos_y_5 = (pos_y_5 + 1) % 2

print("You hit %s trees." % hits_1)

print("Product of hits: %s" % (hits_1 * hits_2 * hits_3 * hits_4 * hits_5,))
