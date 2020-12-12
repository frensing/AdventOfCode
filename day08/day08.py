acc = 0

code_lines = []
visited = []
found_loop = False
current_line_number = 0

with open('input.txt', 'r') as input:
    for line in input:
        instruction = line.strip().split()
        code_lines.append((instruction[0], int(instruction[1])))

while not found_loop:
    if current_line_number in visited:
        break
    visited.append(current_line_number)
    current_line = code_lines[current_line_number]
    if current_line[0] == 'jmp':
        current_line_number += current_line[1]
        continue
    if current_line[0] == 'acc':
        acc += current_line[1]
    current_line_number += 1

print("Part 1:", acc)
