# Advent of Code 2020 Day 11 Part 1 solution
# Cyrus Sadeghi

import copy

def get_index(row, col, max_cols):
    return col + (row * max_cols)

def count_adjacent(row, col, seat_map, max_rows, max_cols):
    idx = get_index(row, col, max_cols)
    adjacent = 0

    if col < max_cols - 1 and seat_map[idx + 1] == '#':
        adjacent = adjacent + 1
    if col > 0 and seat_map[idx - 1] == '#':
        adjacent = adjacent + 1
    if row < max_rows - 1 and seat_map[get_index(row + 1, col, max_cols)] == '#':
        adjacent = adjacent + 1
    if row > 0 and seat_map[get_index(row - 1, col, max_cols)] == '#':
        adjacent = adjacent + 1
    if col < max_cols - 1 and row < max_rows - 1 and seat_map[get_index(row + 1, col + 1, max_cols)] == '#':
        adjacent = adjacent + 1
    if col < max_cols - 1 and row > 0 and seat_map[get_index(row - 1, col + 1, max_cols)] == '#':
        adjacent = adjacent + 1
    if col > 0 and row < max_rows - 1 and seat_map[get_index(row + 1, col - 1, max_cols)] == '#':
        adjacent = adjacent + 1
    if col > 0 and row > 0 and seat_map[get_index(row - 1, col - 1, max_cols)] == '#':
        adjacent = adjacent + 1

    return adjacent

def main():
    seat_map_file = open('input.txt', 'r')
    seat_map = list()
    old_seat_map = list()
    rows = 0
    cols = 0
    cols_set = False

    for row in seat_map_file:
        for seat in row:
            if seat == '\n':
                continue

            seat_map.append(seat)
            
            if cols_set == False:
                cols = cols + 1

        cols_set = True
        rows = rows + 1

    while seat_map != old_seat_map:
        old_seat_map = copy.deepcopy(seat_map)

        row = 0
        col = 0

        while row < rows and col < cols:
            seat_idx = get_index(row, col, cols)
            seat = seat_map[seat_idx]
            adjacent = count_adjacent(row, col, old_seat_map, rows, cols)

            col = col + 1

            if col == cols:
                col = 0
                row = row + 1

            if seat == '.':
                continue
            elif seat == 'L' and adjacent == 0:
                seat_map[seat_idx] = '#'
            elif seat == '#' and adjacent >= 4:
                seat_map[seat_idx] = 'L'

    print(seat_map.count('#'))

main()