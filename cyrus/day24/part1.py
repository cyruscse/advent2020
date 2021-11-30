# Advent of Code 2020 Day 24 Part 1 solution
# Cyrus Sadeghi

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

    print(len(black))


main()