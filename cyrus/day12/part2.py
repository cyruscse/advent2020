# Advent of Code 2020 Day 12 Part 2 solution
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

def waypoint_angle(value, waypoint_pos):
    positions = [[waypoint_pos[0], waypoint_pos[1]], [0 - waypoint_pos[1], waypoint_pos[0]], [0 - waypoint_pos[0], 0 - waypoint_pos[1]], [waypoint_pos[1], 0 - waypoint_pos[0]]]
    return positions[value]

def main():
    directions = open('input.txt', 'r')
    pos = [0, 0]
    waypoint_pos = [10, -1]

    for direction in directions:
        action = direction[0]
        value = int(direction[1:])

        if action == 'N' or action == 'E' or action == 'W' or action == 'S':
            waypoint_pos = news_move(waypoint_pos, action, value)
        elif action == 'R':
            waypoint_pos = waypoint_angle(int(value / 90), waypoint_pos)
        elif action == 'L':
            waypoint_pos = waypoint_angle(0 - int(value / 90), waypoint_pos)
        elif action == 'F':
            pos = [pos[0] + waypoint_pos[0] * value, pos[1] + waypoint_pos[1] * value]

    print(abs(pos[0]) + abs(pos[1]))

main()