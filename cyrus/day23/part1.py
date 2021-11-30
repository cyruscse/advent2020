# Advent of Code 2020 Day 23 Part 1 solution
# Cyrus Sadeghi

def main():
    seed = '219748365'
    lowest = int(list(seed)[0])
    highest = lowest
    cups = list()
    current = 0
    turns = 100

    for digit in list(seed):
        cups.append(int(digit))

        if int(digit) < lowest:
            lowest = int(digit)

        if int(digit) > highest:
            highest = int(digit)

    olen = len(cups)

    while turns != 0:
        print((101 - turns), cups)
        pickup = list()
        pickup_idx = current + 1
        destination = cups[current] - 1
        current_idx = current
        current_cup = cups[current]

        if destination == 0:
            destination = highest

        while len(pickup) != 3:
            if pickup_idx == len(cups):
                pickup_idx = 0
            pickup.append(cups.pop(pickup_idx))

        print('three_cups=', pickup)

        while destination not in cups:
            if destination < lowest:
                destination = highest
                continue

            destination = destination - 1

        destination_idx = cups.index(destination) + 1

        print('destination=', destination)

        for picked in pickup:
            cups.insert(destination_idx, picked)
            destination_idx = destination_idx + 1

            if destination_idx == olen:
                destination_idx = 0

        current = cups.index(current_cup) + 1

        if current == len(cups):
            current = 0

        turns = turns - 1

    print(cups)

main()
