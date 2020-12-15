# Advent of Code 2020 Day 14 Part 2 solution
# Cyrus Sadeghi

from collections.abc import Iterable
import copy

def binary_tree(bits):
    if len(bits) == 0:
        return [1, 0]

    bits.pop()
    result = binary_tree(bits)
    retlist = list()
    for res in result:
        retlist.append([1, res])
        retlist.append([0, res])
    return retlist

# thanks stackoverflow
def unwind(list):
    for el in list:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            yield from unwind(el)
        else:
            yield el

def parse_mask(value, mask_bin):
    idx = 35
    bits = list()
    addresses = list()

    for char in mask_bin:
        if char == '1':
            value = int(value) | pow(2, idx)
        elif char == 'X':
            value = int(value) & ~pow(2, idx)
            bits.append(pow(2, idx))

        idx = idx - 1

    bits_copy = copy.deepcopy(bits)
    bits.pop()
    combos = binary_tree(bits)

    for nested in combos:
        floating = list(unwind(nested))
        idx = 0
        address = 0
        val = value

        for combo in floating:
            val = val | (combo * bits_copy[idx])
            idx = idx + 1

        addresses.append(val)

    return addresses

def main():
    program = open('input.txt', 'r')
    memory = dict()
    mask = 0

    for line in program:
        if line.split()[0] == 'mask':
            mask = line.split()[2]
        else:
            val = int(line.split()[2])
            addresses = parse_mask(line.split()[0].strip(']')[4:], mask)

            for pos in addresses:
                memory[pos] = val

    sum = 0

    for address in memory.keys():
        sum = sum + memory[address]

    print(sum)

main()