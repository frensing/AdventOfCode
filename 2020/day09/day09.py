numbers = []
preamble_len = 25
preamble = []


def check_number(number):
    for i in range(preamble_len - 1):
        for j in range(i + 1, preamble_len):
            if preamble[i] + preamble[j] == number:
                return True
    return False


def find_sum(number):
    index_num = numbers.index(number)
    for i in range(index_num):
        sum = numbers[i]
        for j in range(i + 1, index_num):
            sum += numbers[j]
            if sum == number:
                used_num = numbers[i:j + 1].copy()
                used_num.sort()
                return used_num[0] + used_num[-1]
            if sum > number:
                break
    return False


with open('input.txt', 'r') as input:
    for line in input:
        numbers.append(int(line.strip()))

for i in range(preamble_len):
    preamble.append(numbers[i])

for num in numbers[preamble_len:]:
    if not check_number(num):
        print("Part 1:", num)
        break
    preamble.pop(0)
    preamble.append(num)

print("Part 2:", find_sum(num))
