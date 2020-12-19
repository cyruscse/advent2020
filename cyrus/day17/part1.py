# Advent of Code 2020 Day 17 Part 1 solution
# Cyrus Sadeghi

import copy

def generate_neighbours(coord):
    neighbours = list()

    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x == 0 and y == 0 and z == 0:
                    continue

                neighbours.append((coord[0] + x, coord[1] + y, coord[2] + z))

    return neighbours

def main():
    grid = open('input.txt', 'r')
    active = list()
    y = 0

    for line in grid:
        x = 0
        for coord in line.strip():
            if coord == '#':
                active.append((x, y, 0))

            x = x + 1
        y = y + 1

    cycle = 0

    while cycle != 6:
        neighbour_occ = dict()
        active_copy = copy.deepcopy(active)
        inactive = set()

        for coord in active:
            neighbour_occ[coord] = generate_neighbours(coord)

        for coord in active:
            occs = 0

            for neighbour in neighbour_occ[coord]:
                if neighbour in active:
                    occs = occs + 1
                else:
                    inactive.add(neighbour)

            if occs != 2 and occs != 3:
                active_copy.remove(coord)

        for coord in inactive:
            neighbour_occ[coord] = generate_neighbours(coord)

        for coord in inactive:
            occs = 0

            for neighbour in neighbour_occ[coord]:
                if neighbour in active:
                    occs = occs + 1

            if occs == 3:
                active_copy.append(coord)

        active = active_copy
        cycle = cycle + 1

    print(len(active))

main()