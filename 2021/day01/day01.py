with open('input.txt', 'r') as input:
    numbers = [int(line.strip()) for line in input]

x1 = sum([1 for i in range(1, len(numbers)) if numbers[i-1] < numbers[i]])

print("Part 1:", x1)

x2 = sum([1 for i in range(3, len(numbers)) if numbers[i-3] < numbers[i]])

print("Part 2:", x2)
