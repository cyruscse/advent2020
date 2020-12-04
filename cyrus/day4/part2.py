# Advent of Code 2020 Day 4 Part 2 solution
# Cyrus Sadeghi

import re

def validate_height(height):
    search_res = re.compile("[^\W\d]").search(height)
    parsed = list()

    if search_res == None:
        return False

    parsed.append(int(height[:search_res.start()]))
    parsed.append(height[search_res.start():])

    if ((parsed[1] == 'cm' and parsed[0] >= 150 and parsed[0] <= 193) or
        (parsed[1] == 'in' and parsed[0] >= 59 and parsed[0] <= 76)):
        return True

    return False

def validate_hcl(hcl):
    parsed = hcl.split('#')

    if len(parsed) != 2 or len(parsed[1]) != 6:
        return False

    for char in parsed[1]:
        if char.isdigit() == False and (char < 'a' or char > 'f'):
            return False

    return True

def validate_ecl(ecl):
    if ecl == 'amb' or ecl == 'blu' or ecl == 'brn' or ecl == 'gry' or ecl == 'grn' or ecl == 'hzl' or ecl == 'oth':
        return True

    return False

def validate_pid(pid):
    if len(pid) == 9 and pid.isdigit():
        return True

    return False

def main():
    entries = open('input.txt', 'r')
    passports = list(dict())
    valid_passports = 0
    idx = 0
    pass_keys = 0
    cid_present = False

    passports.append(dict())

    for line in entries:
        kvs = line.split()

        for pair in kvs:
            key = pair.split(':')[0]
            value = pair.split(':')[1]

            passports[idx][key] = value
            
            if ((key == 'byr' and int(value) >= 1920 and int(value) <= 2002) or 
                (key == 'iyr' and int(value) >= 2010 and int(value) <= 2020) or
                (key == 'eyr' and int(value) >= 2020 and int(value) <= 2030) or
                (key == 'hgt' and validate_height(value)) or
                (key == 'hcl' and validate_hcl(value)) or
                (key == 'ecl' and validate_ecl(value)) or
                (key == 'pid' and validate_pid(value))):
                pass_keys = pass_keys + 1

            if key == 'cid':
                pass_keys = pass_keys + 1
                cid_present = True

        if len(line) == 1:
            if (pass_keys == 8) or (pass_keys == 7 and cid_present == False):
                valid_passports = valid_passports + 1

            pass_keys = 0
            cid_present = False
            passports.append(dict())
            idx = idx + 1
            continue

    print(valid_passports)

main()