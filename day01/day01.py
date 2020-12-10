with open('day01_input.txt', 'r') as input:
    numbers = [int(line.strip()) for line in input]

for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        x = numbers[i]
        y = numbers[j]
        if x + y == 2020:
            print("%s + %s = %s" % (x, y, x * y))
        for k in range(j + 1, len(numbers)):
            z = numbers[k]
            if x + y + z == 2020:
                print("%s + %s + %s = %s" % (x, y, z, x * y * z))
