def get_counts(group, members):
    c_1 = len(group.keys())
    c_2 = 0
    for v in group.values():
        if v == members:
            c_2 += 1
    return (c_1, c_2)


with open('input.txt', 'r') as input:
    group = {}
    counts_1 = 0
    counts_2 = 0
    members = 0
    for line in input:
        line = line.strip()
        if line == '':
            counts = get_counts(group, members)
            counts_1 += counts[0]
            counts_2 += counts[1]
            members = 0
            group = {}
            continue
        for c in line:
            if c not in group:
                group[c] = 0
            group[c] += 1
        members += 1
    counts = get_counts(group, members)
    counts_1 += counts[0]
    counts_2 += counts[1]

    print("Part 1:", counts_1)
    print("Part 2:", counts_2)
