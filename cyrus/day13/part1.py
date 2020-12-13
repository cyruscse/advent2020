# Advent of Code 2020 Day 13 Part 1 solution
# Cyrus Sadeghi

def main():
    schedules_file = open('input.txt', 'r')
    schedules = schedules_file.readlines()
    idx = 0

    arrival = int(schedules[0])
    buses = schedules[1].strip().split(',')
    closest_arrival = -1
    best_bus = 0

    for bus in buses:
        if bus == 'x':
            continue

        bus = int(bus)
        good_depart = 0
        idx = 0

        while good_depart < arrival:
            good_depart = bus * idx
            idx = idx + 1

        if closest_arrival == -1 or good_depart - arrival < closest_arrival:
            best_bus = bus
            closest_arrival = good_depart - arrival

    print(best_bus * closest_arrival)

main()