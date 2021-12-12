with open('input.txt', 'r') as inp:
    graph = {}
    big_caves = []
    small_caves = []

    for line in inp:
        x, y = line.strip().split('-')

        if x.upper() == x:
            big_caves.append(x)
        elif x not in ['start', 'end']:
            small_caves.append(x)
        if y.upper() == y:
            big_caves.append(y)
        elif y not in ['start', 'end']:
            small_caves.append(y)

        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []

        graph[x].append(y)
        graph[y].append(x)

paths = []


def explore_from_node(node, path, special_cave=(None, False)):
    if node == 'end':
        path.append('end')

        path_str = ','.join(path)
        if path_str not in paths:
            paths.append(path_str)

        path.pop()
        return

    if node not in big_caves and node in path:
        if node == special_cave[0] and special_cave[1]:
            special_cave[1] = False
        else:
            return

    path.append(node)

    for neighbour in graph[node]:
        explore_from_node(neighbour, path, special_cave)

    path.pop()

    if node == special_cave[0] and not special_cave[1]:
        special_cave[1] = True


explore_from_node('start', [])

print("Part 1:", len(paths))

for cave in small_caves:
    explore_from_node('start', [], [cave, True])

print("Part 2:", len(paths))
