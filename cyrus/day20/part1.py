# Advent of Code 2020 Day 20 Part 1 solution
# Cyrus Sadeghi

def rotate(layout):
    rlayout = list()
    rlayout.append(layout[3][::-1])
    rlayout.append(layout[0])
    rlayout.append(layout[1][::-1])
    rlayout.append(layout[2])

    return rlayout

def main():
    in_file = open('testinput.txt', 'r')
    tile_layout = dict()
    tile = 0
    layout = list()
    lcol = str()
    rcol = str()
    idx = 0

    for line in in_file:
        if line == '\n':
            continue

        if 'Tile' in line:
            if tile != 0:
                layout.append(rcol)
                layout.append(lcol)
                layout[1], layout[2] = layout[2], layout[1]
                tile_layout[int(tile)] = layout
            tile = line[5:-2]
            layout = list()
            lcol = str()
            rcol = str()
            idx = 0
            continue

        lcol = lcol + line[0]
        rcol = rcol + line[9]

        if idx == 0:
            layout.append(line.strip())
        elif idx == 9:
            layout.append(line.strip())

        idx = idx + 1

    for tidx in tile_layout.keys():
        for ctidx in tile_layout.keys():
            if tidx == ctidx:
                continue

            adjacencies = 0
            rotate_counter = 4
            rlayout = tile_layout[tidx]

            while rotate_counter != 0:
                crotate_counter = 4
                trlayout = tile_layout[ctidx]

                while crotate_counter != 0:
                    rlayouts = set(rlayout)
                    trlayouts = set(trlayout)



                    trlayout = rotate(trlayout)
                    crotate_counter = crotate_counter - 1

                rlayout = rotate(rlayout)
                rotate_counter = rotate_counter - 1

main()
