def get_pos(boundaries, input):
    def update_value(bounds):
        return (bounds[1] + bounds[0]) // 2

    for c in input:
        if c == 'F' or c == 'L':
            boundaries[1] = update_value(boundaries)
        else:
            boundaries[0] = update_value(boundaries) + 1
    return boundaries[0]


with open('input.txt', 'r') as input:
    highest_id = 0
    seat_ids = []

    for line in input:
        line = line.strip()
        row = get_pos([0, 127], line[:7])
        col = get_pos([0, 7], line[7:])
        id = row * 8 + col

        seat_ids.append(id)

        if highest_id < id:
            highest_id = id

    seat_ids.sort()
    seat = -1
    for i in range(1, len(seat_ids) - 1):
        if seat_ids[i - 1] != seat_ids[i] - 1:
            seat = seat_ids[i] - 1

    print("Part 1:", highest_id)
    print("Part 2:", seat)
