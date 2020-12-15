# Advent of Code 2020 Day 15 Part 1 solution
# Cyrus Sadeghi

def main():
    input = [1, 2, 16, 19, 18, 0]
    last_spoken = dict()
    last_number = 0
    idx = 0

    for val in input:
        if idx != len(input) - 1:
            last_spoken[val] = idx
        last_number = val
        idx = idx + 1

    idx = idx - 1

    while idx != 29999999:
        if last_number not in last_spoken.keys():
            last_spoken[last_number] = idx
            last_number = 0
        else:
            new_last_number = idx - last_spoken[last_number]
            last_spoken[last_number] = idx
            last_number = new_last_number

        idx = idx + 1

    print(last_number)

main()
