with open('input.txt', 'r') as inp:
    init_state = list(map(int, inp.readline().strip().split(',')))


def calc_population(init_state, days):
    state = [0] * 9
    for x in init_state:
        state[x] += 1

    for d in range(days):
        new_state = [state[i] for i in range(1, len(state))] + [0]

        new_state[8] = state[0]
        new_state[6] += state[0]

        state = new_state
    return sum(state)


print("Part 1:", calc_population(init_state, 80))
print("Part 2:", calc_population(init_state, 256))
