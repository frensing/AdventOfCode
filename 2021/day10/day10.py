with open('input.txt', 'r') as inp:
    lines = [line.strip() for line in inp]

closing_chars = {'(': ')', '[': ']', '{': '}', '<': '>'}
closing_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
completion_points = {')': 1, ']': 2, '}': 3, '>': 4}

corrupted_chars = []

completions = []

for line in lines:
    chunks = []

    corrupted = False

    for e in line:
        if e in '([{<':
            chunks.append(e)
            continue

        cur_chunk = chunks.pop()
        if e != closing_chars[cur_chunk]:
            corrupted_chars.append(e)
            corrupted = True
            break

    if not corrupted:
        completions.append(closing_chars[e] for e in chunks[::-1])

print("Part 1:", sum(closing_points[e] for e in corrupted_chars))

points = []
for compl in completions:
    p = 0
    for e in compl:
        p = p * 5 + completion_points[e]
    points.append(p)

print("Part 2:", sorted(points)[len(points) // 2])
