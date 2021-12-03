with open('input.txt', 'r') as inp:
    report = [line.strip() for line in inp]

############# Part 1 ##########

gamma_bits = [0] * len(report[0])

for i in range(len(gamma_bits)):
    gamma_bits[i] = 1 if sum(int(entry[i]) for entry in report) / len(report) >= 0.5 else 0

gamma = int(''.join(str(b) for b in gamma_bits), 2)
epsilon = int(''.join(str(b) for b in [abs(x - 1) for x in gamma_bits]), 2)

print("Part 1:", gamma * epsilon)


############# Part 2 #################

def get_rating(report, bit_func):
    keep = list(range(len(report)))

    for i in range(len(report[0])):
        most_common = bit_func(i, keep)

        tmp = [x for x in keep if int(report[x][i]) == most_common]

        if len(tmp) == 1:
            return report[tmp[0]]

        keep = tmp


oxygen_func = lambda i, keep: 1 if sum(int(report[j][i]) for j in keep) / len(keep) >= 0.5 else 0
co2_func = lambda i, keep: abs(oxygen_func(i, keep) - 1)

oxygen = int(''.join(get_rating(report, oxygen_func)), 2)
co2 = int(''.join(get_rating(report, co2_func)), 2)

print("Part 2:", oxygen * co2)
