# Advent of Code 2020 Day 13 Part 2 solution
# Cyrus Sadeghi

def main():
    schedules_file = open('input.txt', 'r')
    schedules = schedules_file.readlines()

    buses_split = schedules[1].strip().split(',')
    buses = []

    for i, bus in enumerate(buses_split):
        if bus == 'x':
            continue

        buses.append((i, int(bus)))

    offset = buses[0][1]
    timestamp = 0

    for idx, bus_id in buses[1:]:
        while (timestamp + idx) % bus_id != 0:
            timestamp += offset
        offset *= bus_id

    print(timestamp)

main()