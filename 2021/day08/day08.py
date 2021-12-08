with open('input.txt', 'r') as inp:
    lines = [[x.split() for x in line.strip().split(' | ')] for line in inp]

print("Part 1:", sum(sum(1 for x in line[1] if len(x) in [2, 3, 4, 7]) for line in lines))

numbers = {0: 'abcefg',
           1: 'cf',
           2: 'acdeg',
           3: 'acdfg',
           4: 'bcdf',
           5: 'abdfg',
           6: 'abdefg',
           7: 'acf',
           8: 'abcdefg',
           9: 'abcdfg'}


def calc_diff(segments, set_keys):
    for seg in segments:
        if seg in set_keys:
            continue
        segments[seg] = segments[seg].difference(*[segments[key] for key in set_keys])


nums = []

for line in lines:

    s = set('abcdefg')
    segments = {'a': s, 'b': s, 'c': s, 'd': s, 'e': s, 'f': s, 'g': s}

    inp = sorted(line[0], key=len)

    for x in inp:
        x = sorted(x)
        if len(x) == 2:
            # number 1
            for seg in numbers[1]:
                segments[seg] = segments[seg].intersection(set(x))

            calc_diff(segments, 'cf')

            continue

        if len(x) == 3:
            # number 7
            segments['c'] = segments['c'].intersection(set(x))
            segments['f'] = segments['f'].intersection(set(x))

            segments['a'] = segments['a'].intersection(set(x).difference(segments['c'], segments['f']))

            calc_diff(segments, 'a')

            continue

        if len(x) == 4:
            # number 4
            segments['c'] = segments['c'].intersection(set(x))
            segments['f'] = segments['f'].intersection(set(x))

            r = set(x).difference(segments['c'], segments['f'])

            segments['b'] = segments['b'].intersection(r)
            segments['d'] = segments['d'].intersection(r)

            calc_diff(segments, 'bd')

            continue

        if len(x) == 5:
            d = set(x).difference(segments['a'], segments['c'], segments['f'])
            if len(d) == 2:
                # number 3
                segments['d'] = segments['d'].intersection(d)
                segments['g'] = segments['g'].intersection(d)

                calc_diff(segments, 'dg')

                continue

            d = set(x).difference(segments['a'], segments['b'], segments['d'], segments['f'], segments['g'])
            if len(d) == 0:
                # number 5 or 2
                d2 = set(x).intersection(segments['b'].union(segments['d']))
                if len(d2) == 2:
                    # number 5
                    segments['f'] = segments['f'].intersection(set(x))
                    segments['c'] = segments['c'].difference(segments['f'])
                else:
                    # number 2
                    segments['c'] = segments['c'].intersection(set(x))
                    segments['f'] = segments['f'].difference(segments['c'])

                continue

    segments = {key: segments[key].pop() for key in segments}
    rewired = {segments[key]: key for key in segments}

    inverted_numbers = {numbers[key]: key for key in numbers}

    out = line[1]
    out_digits = []
    for x in out:
        segs = ''.join(sorted([rewired[e] for e in x]))
        out_digits.append(inverted_numbers[segs])

    nums.append(int(''.join(str(x) for x in out_digits)))


print("Part 2:", sum(nums))
