# Advent of Code 2020 Day 12 Part 1 solution
# Cyrus Sadeghi

def news_move(pos, action, value):
    if action == 'N':
        return [pos[0], pos[1] - value]
    elif action == 'S':
        return [pos[0], pos[1] + value]
    elif action == 'E':
        return [pos[0] + value, pos[1]]
    elif action == 'W':
        return [pos[0] - value, pos[1]]

def main():
    directions = open('input.txt', 'r')
    pos = [0, 0]
    facing = 'E'
    compass = ['N', 'E', 'S', 'W']

    for direction in directions:
        action = direction[0]
        value = int(direction[1:])

        if action == 'N' or action == 'E' or action == 'W' or action == 'S':
            pos = news_move(pos, action, value)
        elif action == 'L':
            value = int(value / 90)
            compass_idx = (compass.index(facing) - value) % 4

            if compass_idx < 0:
                compass_idx = compass_idx + 4

            facing = compass[compass_idx]
        elif action == 'R':
            value = int(value / 90)
            compass_idx = (compass.index(facing) + value) % 4

            if compass_idx > 3:
                compass_idx = compass_idx - 4

            facing = compass[compass_idx]
        elif action == 'F':
            pos = news_move(pos, facing, value)

    print(abs(pos[0]) + abs(pos[1]))

main()