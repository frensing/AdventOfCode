with open('input.txt', 'r') as inp:
    sequence = [int(n) for n in inp.readline().split(',')]

    inp.readline()
    fields = []
    field = []
    for line in inp:
        l = line.strip()
        if l == '':
            fields.append(field)
            field = []
            continue

        field.extend([int(n) for n in l.split()])
    else:
        fields.append(field)

    del field


def check_bingo(field, sequence):
    res_lines = _check_lines(field, sequence)
    if res_lines:
        return res_lines

    res_columns = _check_columns(field, sequence)
    if res_columns:
        return res_columns

    return None


def _check_lines(field, sequence):
    for i in range(0, 21, 5):
        if all(field[j] in sequence for j in range(i, i + 5)):
            return get_sum(field, sequence)
    return None


def _check_columns(field, sequence):
    for x in range(5):
        if all(field[y] in sequence for y in range(x, x + 21, 5)):
            return get_sum(field, sequence)
    return None


def get_sum(field, sequence):
    return sum(cell for cell in field if cell not in sequence)


def check_win_fields(fields, sequence):
    for x in range(4, len(sequence)):
        for f in fields:
            res = check_bingo(f, sequence[0:x + 1])
            if res:
                return res * sequence[x]


def check_loose_fields(fields, sequence):
    win_boards = []
    for x in range(4, len(sequence)):
        for f in fields:
            if f in win_boards:
                continue
            res = check_bingo(f, sequence[0:x + 1])
            if res:
                win_boards.append(f)
                if len(win_boards) == len(fields):
                    return res * sequence[x]


print("Part 1:", check_win_fields(fields, sequence))
print("Part 2:", check_loose_fields(fields, sequence))
