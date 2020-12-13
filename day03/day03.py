with open('input.txt', 'r') as input:
    lines = [line.strip() for line in input]


def get_hits(slope):
    pos = [0, 0]
    hits = 0
    for line in lines:
        if line[pos[0]] == '#' and pos[1] == 0:
            hits += 1
        if pos[1] == 0:
            pos[0] = (pos[0] + slope[0]) % len(line)
        pos[1] = (pos[1] + 1) % slope[1]
    return hits


slopes = [[3, 1], [1, 1], [5, 1], [7, 1], [1, 2]]

result_2 = 1
for slope in slopes:
    result_2 *= get_hits(slope)

print("You hit %s trees." % get_hits(slopes[0]))

print("Product of hits: %s" % result_2)
