with open('input.txt', 'r') as input:
    lines = [line.strip().replace(':', '').split() for line in input]

first_valid_count = 0
second_valid_count = 0

for line in lines:
    word = line[2]
    char = line[1]
    count = word.count(char)
    low, high = [int(elm) for elm in line[0].split('-')]
    if low <= count <= high:
        first_valid_count += 1
    if (word[low - 1] == char or word[high - 1] == char) and word[low - 1] != word[high - 1]:
        second_valid_count += 1

print("First valid count:  %s" % first_valid_count)
print("Second valid count: %s" % second_valid_count)
