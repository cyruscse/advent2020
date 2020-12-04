# Advent of Code 2020 Day 4 Part 1 solution
# Cyrus Sadeghi

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
            pass_keys = pass_keys + 1

            if key == 'cid':
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