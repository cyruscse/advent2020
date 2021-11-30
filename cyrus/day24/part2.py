# Advent of Code 2020 Day 24 Part 2 solution
# Cyrus Sadeghi

def get_adjacent(tile):
    adjacent = set()

    # e
    adjacent.add((tile[0] + 1, tile[1]))
    # w
    adjacent.add((tile[0] - 1, tile[1]))
    # ne
    adjacent.add((tile[0] + 0.5, tile[1] - 1))
    # se
    adjacent.add((tile[0] + 0.5, tile[1] + 1))
    # sw
    adjacent.add((tile[0] - 0.5, tile[1] + 1))
    # nw
    adjacent.add((tile[0] - 0.5, tile[1] - 1))

    return adjacent

def main():
    in_file = open('input.txt', 'r')
    tiles = list()
    black = set()

    for in_line in in_file:
        idx = 0
        processing = False
        process_letter = ''
        directions = list()

        for letter in in_line:
            if letter == 'e' or letter == 'w':
                if processing == False:
                    directions.append(letter)
                else:
                    directions.append(process_letter + letter)
                    process_letter = ''
                    processing = False
            else:
                if processing == True:
                    directions.append(process_letter)
                    directions.append(letter)
                    process_letter = ''
                    processing = False
                else:
                    process_letter = letter
                    processing = True
        tiles.append(directions)

    for tile in tiles:
        coordinate = [0, 0]

        for direction in tile:
            if direction == 'e':
                coordinate[0] = coordinate[0] + 1
            elif direction == 'w':
                coordinate[0] = coordinate[0] - 1
            elif direction == 'ne':
                coordinate[1] = coordinate[1] - 1
                coordinate[0] = coordinate[0] + 0.5
            elif direction == 'se':
                coordinate[1] = coordinate[1] + 1
                coordinate[0] = coordinate[0] + 0.5
            elif direction == 'sw':
                coordinate[1] = coordinate[1] + 1
                coordinate[0] = coordinate[0] - 0.5
            elif direction == 'nw':
                coordinate[1] = coordinate[1] - 1
                coordinate[0] = coordinate[0] - 0.5

        tcoord = (coordinate[0], coordinate[1])

        if tcoord in black:
            black.remove(tcoord)
        else:
            black.add(tcoord)

    for i in range(0, 100):
        adj_tiles = dict()
        new_white = set()
        new_black = set()

        for tile in black:
            adj_tiles[tile] = get_adjacent(tile)
            adjacencies = 0
            adj_blacks = len(black & adj_tiles[tile])

            if adj_blacks == 0 or adj_blacks > 2:
                new_white.add(tile) 

        white_adj = dict()

        for tile in black:
            for adjacent in adj_tiles[tile]:
                if adjacent in black:
                    continue

                if adjacent not in white_adj.keys():
                    white_adj[adjacent] = 1
                else:
                    white_adj[adjacent] = white_adj[adjacent] + 1

        for testwhite in white_adj.keys():
            if white_adj[testwhite] == 2:
                new_black.add(testwhite)

        for white in new_white:
            black.remove(white)

        for nblack in new_black:
            black.add(nblack)

    print(len(black))

main()