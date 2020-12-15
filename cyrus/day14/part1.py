# Advent of Code 2020 Day 14 Part 1 solution
# Cyrus Sadeghi

def parse_mask(value, mask_bin):
    idx = 35
    val = value

    for char in mask_bin:
        if char == '1':
            val = val | pow(2, idx)
        elif char == '0':
            val = val & ~pow(2, idx)

        idx = idx - 1

    return val

def main():
    program = open('input.txt', 'r')
    memory = dict()
    mask = 0

    for line in program:
        if line.split()[0] == 'mask':
            mask = line.split()[2]
        else:
            val = parse_mask(int(line.split()[2]), mask)
            pos = line.split()[0].strip(']')[4:]

            memory[pos] = val

    sum = 0

    for address in memory.keys():
        sum = sum + memory[address]

    print(sum)

main()