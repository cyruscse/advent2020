# Advent of Code 2020 Day 3 Part 1 solution
# Cyrus Sadeghi

def main():
    trees = open('input.txt', 'r')
    layout = list(list())
    pos_x = 0
    pos_y = 0
    encountered = 0

    for line in trees:
        this_line = list()

        for entry in line:
            if entry == '\n':
                break

            this_line.append(entry)

        layout.append(this_line)

    while pos_y != len(layout):
        if pos_x > len(layout[0]):
            bounded_pos_x = pos_x % len(layout[0])
        else:
            bounded_pos_x = pos_x

        if layout[pos_y][bounded_pos_x] == '#':
            encountered = encountered + 1

        pos_x = pos_x + 3
        pos_y = pos_y + 1

    print(encountered)

main()