import re

p_fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
ecl_values = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def is_valid_1(passport):
    for field in p_fields:
        if field not in passport:
            return False
    return True


def is_valid_2(passport):
    if not is_valid_1(passport): return False

    if not (1920 <= int(passport[p_fields[0]]) <= 2002): return False
    if not (2010 <= int(passport[p_fields[1]]) <= 2020): return False
    if not (2020 <= int(passport[p_fields[2]]) <= 2030): return False
    if re.fullmatch(r'#[0-9a-f]{6}', passport[p_fields[4]]) is None: return False
    if passport[p_fields[5]] not in ecl_values: return False
    if re.fullmatch(r'[0-9]{9}', passport[p_fields[6]]) is None: return False

    hgt = passport[p_fields[3]]
    if re.fullmatch(r'1[0-9]{2}cm|[5-7][0-9]in', hgt) is None: return False
    if hgt[-2:] == 'cm' and not (150 <= int(hgt[:-2]) <= 193): return False
    if hgt[-2:] == 'in' and not (59 <= int(hgt[:-2]) <= 76): return False

    return True


with open('input.txt', 'r') as input:
    passport = {}
    valid_1 = 0
    valid_2 = 0
    for line in input:
        l = line.strip()
        if l == '':
            if is_valid_1(passport):
                valid_1 += 1
            if is_valid_2(passport):
                valid_2 += 1
            passport = {}
            continue

        fields = l.split()
        for field in fields:
            k, v = field.split(':')
            passport[k] = v

    print("Valid_1 passports: %s" % valid_1)
    print("Valid_2 passports: %s" % valid_2)
