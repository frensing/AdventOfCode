with open('input.txt', 'r') as inp:
    field = [[int(x) for x in line.strip()] for line in inp]

minimums = []
minimums_coord = []

for y in range(len(field)):
    for x in range(len(field[0])):
        cell = field[y][x]
        is_minimum = True
        if y > 0:
            if field[y - 1][x] <= cell:
                is_minimum = False
                continue
        if x > 0:
            if field[y][x - 1] <= cell:
                is_minimum = False
                continue

        if x < len(field[0]) - 1:
            if field[y][x + 1] <= cell:
                is_minimum = False
                continue

        if y < len(field) - 1:
            if field[y + 1][x] <= cell:
                is_minimum = False
                continue

        if is_minimum:
            minimums.append(cell)
            minimums_coord.append((x, y))

print("Part 1:", sum(minimums) + len(minimums))

field = [[x == 9 for x in line] for line in field]

basin_count = 0
coordinates = {}


def flood_fill(visited, coordinate, basin):
    if coordinate in visited:
        return

    x, y = coordinate

    if field[y][x]:
        return

    visited[coordinate] = basin

    if y > 0:
        flood_fill(visited, (x, y - 1), basin)
    if x > 0:
        flood_fill(visited, (x - 1, y), basin)
    if y < len(field) - 1:
        flood_fill(visited, (x, y + 1), basin)
    if x < len(field[0]) - 1:
        flood_fill(visited, (x + 1, y), basin)


for minimum in minimums_coord:
    if minimum in coordinates:
        continue
    basin_count += 1

    flood_fill(coordinates, minimum, basin_count)

basins = {}
for key in coordinates:
    basin = coordinates[key]
    if basin not in basins:
        basins[basin] = 0
    basins[coordinates[key]] += 1

max_3_basin_sizes = sorted([basins[key] for key in basins])[-3:]

product = 1
for x in max_3_basin_sizes:
    product *= x

print("Part 2:", product)
