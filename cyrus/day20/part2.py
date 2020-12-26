# Advent of Code 2020 Day 20 Part 1 solution
# Cyrus Sadeghi

import copy

def rotate(l):
    return [l[1], l[3], l[0], l[2]]

def main():
    tile_file = open('input2.txt', 'r')
    lines = tile_file.readlines()
    num_lines = sum(1 for line in open('input2.txt'))
    id_tiles = dict()
    id_neighbours = dict()
    id_edge_orientation = dict()
    id_orientation = dict()
    allowed_matches = {0: 3, 1: 2, 2: 1, 3: 0}
    edges = dict()
    row = 0
    edge_id = 0
    col_one = list()
    col_two = list()
    line_idx = 0

    while True:
        if line_idx < num_lines:
            line = lines[line_idx]

        if line == '\n' or line_idx == num_lines + 1:
            rev_col_one = list(reversed(col_one))

            if col_one not in edges.values() and rev_col_one not in edges.values():
                cocopy = copy.deepcopy(col_one)
                edges[edge_id] = cocopy
                edge_id = edge_id + 1

            if col_one in edges.values():
                id_tiles[id].append(list(edges.keys())[list(edges.values()).index(col_one)])
                id_edge_orientation[id][1] = 'left col'
            elif rev_col_one in edges.values():
                id_tiles[id].append(list(edges.keys())[list(edges.values()).index(rev_col_one)])
                id_edge_orientation[id][1] = '!left col'

            rev_col_two = list(reversed(col_two))

            if col_two not in edges.values() and rev_col_two not in edges.values():
                ctcopy = copy.deepcopy(col_two)
                edges[edge_id] = ctcopy
                edge_id = edge_id + 1

            if col_two in edges.values():
                id_tiles[id].append(list(edges.keys())[list(edges.values()).index(col_two)])
                id_edge_orientation[id][2] = 'right col'
            elif rev_col_two in edges.values():
                id_tiles[id].append(list(edges.keys())[list(edges.values()).index(rev_col_two)])
                id_edge_orientation[id][2] = '!right col'

            if line_idx == num_lines + 1:
                break
        elif ':' in line:
            id = line.split(' ')[1][:-2]
            id_tiles[id] = list()
            id_edge_orientation[id] = [0 for _ in range(4)]
            id_orientation[id] = 0
            col_one = list()
            col_two = list()
            row = 0
        else:
            if row == 0 or row == 9:
                read_line = list()

                for char in line.strip():
                    read_line.append(char)

                rev_read_line = list(reversed(read_line))

                if read_line not in edges.values() and rev_read_line not in edges.values():
                    rlcopy = copy.deepcopy(read_line)
                    edges[edge_id] = rlcopy
                    edge_id = edge_id + 1

                if read_line in edges.values():
                    id_tiles[id].append(list(edges.keys())[list(edges.values()).index(read_line)])
                    if row == 0:
                        id_edge_orientation[id][0] = 'top row'
                    else:
                        id_edge_orientation[id][3] = 'bottom row'
                elif rev_read_line in edges.values():
                    id_tiles[id].append(list(edges.keys())[list(edges.values()).index(rev_read_line)])
                    if row == 0:
                        id_edge_orientation[id][0] = '!top row'
                    else:
                        id_edge_orientation[id][3] = '!bottom row'

            if row < 10:
                col_one.append(line[0])
                col_two.append(line[9])
            row = row + 1

        line_idx = line_idx + 1

    for id in id_tiles.keys():
        id_neighbours[id] = set()

        for match_id in id_tiles.keys():
            if id == match_id:
                continue

            if len(set(id_tiles[id]).intersection(set(id_tiles[match_id]))) > 0:
                id_neighbours[id].add(match_id)

    remaining_ids = copy.deepcopy(list(id_tiles.keys()))

    while len(remaining_ids) != 0:
        id = remaining_ids.pop()
        possibilites = list()

        '''print(id)
        print(id_tiles[id])
        print(id_orientation[id])
        print(id_edge_orientation[id])'''

        for match_id in id_neighbours[id]:
            my_idx = id_tiles[id].index(set(id_tiles[id]).intersection(set(id_tiles[match_id])).pop())
            neigh_idx = id_tiles[match_id].index(set(id_tiles[id]).intersection(set(id_tiles[match_id])).pop())
            combos = list()

            print(id_tiles[match_id])

            while len(combos) != 4:
                while neigh_idx != allowed_matches[my_idx]:
                    rotated = rotate(id_tiles[match_id])
                    print(rotated)
                    return
                    #neigh_idx = id_tiles[match_id].index(set(id_tiles[id]).intersection(set(id_tiles[match_id])).pop())

                combos.append(my_orientation, other_orientation)

            print(id_tiles[match_id])
            print(neigh_idx)

        return

main()