with open('input.txt', 'r') as inp:
    crabs = list(map(int, inp.readline().strip().split(',')))

median = sorted(crabs)[len(crabs) // 2]

fuel_consumption = sum(abs(median - crab) for crab in crabs)

print("Part 1:", fuel_consumption)


def get_consumption(point):
    return sum(sum(i for i in range(1, abs(point - crab) + 1)) for crab in crabs)


avg = sum(crabs) / len(crabs)
r = sum(crabs) % len(crabs)

if r != 0:
    fuel_consumption = get_consumption(int(avg))
    avg2 = round(avg)
    if int(avg) != avg2:
        f2 = get_consumption(avg2)
        fuel_consumption = fuel_consumption if fuel_consumption < f2 else f2
else:
    fuel_consumption = get_consumption(avg)

print("Part 2:", fuel_consumption)
