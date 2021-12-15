import math


class Node:
    def __init__(self, w, neigh):
        self.w = w
        self.neigh = neigh


with open('input.txt', 'r') as inp:
    field = [[int(x) for x in line.strip()] for line in inp]

graph = {}
for y in range(len(field)):
    for x in range(len(field[0])):
        w = field[y][x]
        neigh = []
        if y > 0:
            neigh.append(','.join((str(x), str(y - 1))))
        if x > 0:
            neigh.append(','.join((str(x - 1), str(y))))
        if y < len(field) - 1:
            neigh.append(','.join((str(x), str(y + 1))))
        if x < len(field[0]) - 1:
            neigh.append(','.join((str(x + 1), str(y))))

        graph[','.join((str(x), str(y)))] = Node(w, neigh)

for node in graph:
    print(node, graph[node].neigh)
print()

start = '0,0'
finish = ','.join([str(len(field[0]) - 1), str(len(field) - 1)])

dist = {node: math.inf for node in graph}
prev = {node: None for node in graph}


def dijkstra(graph, start):
    q = {node: graph[node] for node in graph}

    dist[start] = 0
    while len(q.keys()) > 0:
        u = sorted(q.items(), key=lambda x: dist[x[0]])[0][0]
        del q[u]

        for v in graph[u].neigh:
            if dist[v] > dist[u] + graph[v].w:
                dist[v] = dist[u] + graph[v].w
                prev[v] = u


dijkstra(graph, start)

n = finish
points = 0
while prev[n]:
    points += graph[n].w
    n = prev[n]

print("Part 1:", points)
