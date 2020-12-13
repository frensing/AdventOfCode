preamble_len = 25
preamble = []


def check_number(number):
    for i in range(preamble_len - 1):
        for j in range(i + 1, preamble_len):
            if preamble[i] + preamble[j] == number:
                return True
    return False


with open('input.txt', 'r') as input:
    for i in range(preamble_len):
        preamble.append(int(next(input).strip()))

    for line in input:
        number = int(line.strip())
        if not check_number(number):
            print("Part 1:", number)
            break
        preamble.pop(0)
        preamble.append(number)
