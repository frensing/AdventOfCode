with open('input.txt', 'r') as inp:
    template = list(inp.readline().strip())

    inp.readline()

    rules = {line.strip().split(' -> ')[0]: line.strip().split(' -> ')[1] for line in inp}

rounds = 10
for j in range(rounds):
    i = 0
    while i < len(template) - 1:
        pair = ''.join(template[i:i + 2])
        if pair in rules:
            template.insert(i + 1, rules[pair])
            i += 1

        i += 1

    print(j)

char_count = {}
for c in template:
    if c not in char_count:
        char_count[c] = 0
    char_count[c] += 1

char_count = sorted(char_count.items(), key=lambda x: x[1])
most_common = int(char_count[-1][1])
least_common = int(char_count[0][1])

print("Part 1:", most_common - least_common)


