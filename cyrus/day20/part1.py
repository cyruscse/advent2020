# Advent of Code 2020 Day 20 Part 1 solution
# Cyrus Sadeghi

import copy
from functools import reduce

def main():
    tile_file = open('input.txt', 'r')
    lines = tile_file.readlines()
    num_lines = sum(1 for line in open('input.txt'))
    id_tiles = dict()
    id_neighbours = dict()
    edges = dict()
    row = 0
    edge_id = 0
    col_one = list()
    col_two = list()
    corners = list()
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
            elif rev_col_one in edges.values():
                id_tiles[id].append(list(edges.keys())[list(edges.values()).index(rev_col_one)])

            rev_col_two = list(reversed(col_two))

            if col_two not in edges.values() and rev_col_two not in edges.values():
                ctcopy = copy.deepcopy(col_two)
                edges[edge_id] = ctcopy
                edge_id = edge_id + 1

            if col_two in edges.values():
                id_tiles[id].append(list(edges.keys())[list(edges.values()).index(col_two)])
            elif rev_col_two in edges.values():
                id_tiles[id].append(list(edges.keys())[list(edges.values()).index(rev_col_two)])

            if line_idx == num_lines + 1:
                break
        elif ':' in line:
            id = line.split(' ')[1][:-2]
            id_tiles[id] = list()
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
                elif rev_read_line in edges.values():
                    id_tiles[id].append(list(edges.keys())[list(edges.values()).index(rev_read_line)])

            if row < 10:
                col_one.append(line[0])
                col_two.append(line[9])
            row = row + 1

        line_idx = line_idx + 1

    for id in id_tiles.keys():
        id_neighbours[id] = 0

        for match_id in id_tiles.keys():
            if id == match_id:
                continue

            id_neighbours[id] = id_neighbours[id] + len(set(id_tiles[id]).intersection(set(id_tiles[match_id])))

        if id_neighbours[id] == 2:
            corners.append(int(id))

    print(reduce(lambda x, y: x*y, corners))

main()