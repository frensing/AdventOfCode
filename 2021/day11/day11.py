with open('input.txt', 'r') as inp:
    field = [[int(x) for x in line.strip()] for line in inp]

flashes = 0


def flash_cell(visited, cell):
    if cell in visited:
        return

    x, y = cell
    field[y][x] += 1

    if field[y][x] > 9:
        visited.append(cell)

        if y > 0:
            flash_cell(visited, (x, y - 1))
            if x > 0:
                flash_cell(visited, (x - 1, y - 1))
            if x < len(field[0]) - 1:
                flash_cell(visited, (x + 1, y - 1))

        if x > 0:
            flash_cell(visited, (x - 1, y))
        if x < len(field[0]) - 1:
            flash_cell(visited, (x + 1, y))

        if y < len(field) - 1:
            flash_cell(visited, (x, y + 1))
            if x > 0:
                flash_cell(visited, (x - 1, y + 1))
            if x < len(field[0]) - 1:
                flash_cell(visited, (x + 1, y + 1))


for i in range(1000):
    # Step 1
    field = [[x + 1 for x in line] for line in field]

    # Step 2
    visited = []
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] > 9:
                flash_cell(visited, (x, y))

    # Step 3
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] > 9:
                field[y][x] = 0
                flashes += 1

    if i == 100:
        print("Part 1:", flashes)

    if all(all(x == 0 for x in line) for line in field):
        print("Part 2:", i + 1)
        break
