import time

with open('input.txt', 'r') as inp:
    template = inp.readline().strip()

    inp.readline()

    rules = {}
    for line in inp:
        key, ins = line.strip().split(' -> ')
        rules[key] = [key[0] + ins, ins + key[1]]

rounds = 10


char_count = {}
for key in rules:
    for c in key:
        if c not in char_count:
            char_count[c] = 0


def dfs(depth, node):
    if depth == 0:
        char_count[node[0]] += 1
        return

    dfs(depth - 1, rules[node][0])
    dfs(depth - 1, rules[node][1])


for i in range(len(template) - 1):
    start = time.time()
    dfs(rounds, template[i:i + 2])
    print(i)
    print(time.time() - start)
    print()

char_count[template[-1]] += 1


print()
for c in char_count:
    print(c, char_count[c])

char_count = sorted(char_count.items(), key=lambda x: x[1])
most_common = int(char_count[-1][1])
least_common = int(char_count[0][1])

print("Part 1:", most_common - least_common)
