code_lines = []

with open('input.txt', 'r') as input:
    for line in input:
        instruction = line.strip().split()
        code_lines.append([instruction[0], int(instruction[1])])


def test_code(code_lines):
    acc = 0
    visited = []
    current_line_number = 0
    while True:
        if current_line_number >= len(code_lines):
            return True, acc
        if current_line_number in visited:
            return False, acc
        visited.append(current_line_number)
        current_line = code_lines[current_line_number]
        if current_line[0] == 'jmp':
            current_line_number += current_line[1]
            continue
        if current_line[0] == 'acc':
            acc += current_line[1]
        current_line_number += 1


print("Part 1:", test_code(code_lines)[1])

for i in range(len(code_lines)):
    result = None
    if code_lines[i][0] == 'nop':
        code_lines[i][0] = 'jmp'
        result = test_code(code_lines)
        code_lines[i][0] = 'nop'
    elif code_lines[i][0] == 'jmp':
        code_lines[i][0] = 'nop'
        result = test_code(code_lines)
        code_lines[i][0] = 'jmp'

    if result is not None and result[0]:
        print("Part 2:", result[1])
        break
