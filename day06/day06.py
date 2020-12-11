with open('input.txt', 'r') as input:
    group = {}
    counts = 0
    for line in input:
        line = line.strip()
        if line == '':
            counts += len(group.keys())
            group = {}
            continue
        for c in line:
            group[c] = None
    counts += len(group.keys())

    print("Part 1:", counts)
