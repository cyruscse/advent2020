# Advent of Code 2020 Day 3 Part 2 solution
# Cyrus Sadeghi

def main():
    trees = open('input.txt', 'r')
    layout = list(list())
    pos_x = 0
    pos_y = 0
    encountered = list()
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    idx = 0

    for line in trees:
        this_line = list()

        for entry in line:
            if entry == '\n':
                break

            this_line.append(entry)

        layout.append(this_line)

    for slope in slopes:
        encountered.append(0)

        while pos_y < len(layout):
            if pos_x >= len(layout[0]):
                bounded_pos_x = pos_x % len(layout[0])
            else:
                bounded_pos_x = pos_x

            if layout[pos_y][bounded_pos_x] == '#':
                encountered[idx] = encountered[idx] + 1

            pos_x = pos_x + slope[0]
            pos_y = pos_y + slope[1]

        idx = idx + 1
        pos_x = 0
        pos_y = 0

    print(encountered[0] * encountered[1] * encountered[2] * encountered[3] * encountered[4])    

main()