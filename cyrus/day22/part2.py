# Advent of Code 2020 Day 22 Part 2 solution
# Cyrus Sadeghi

def combat(p1_stack, p2_stack):
    p1_history = list()
    p2_history = list()

    while len(p1_stack) != 0 and len(p2_stack) != 0:
        if p1_stack in p1_history or p2_stack in p2_history:
            return True

        p1_history.append(p1_stack[:])
        p2_history.append(p2_stack[:])

        p1_val = p1_stack.pop(0)
        p2_val = p2_stack.pop(0)

        if p1_val <= len(p1_stack) and p2_val <= len(p2_stack):
            winner = combat(p1_stack[:p1_val], p2_stack[:p2_val])
        else:
            winner = p1_val > p2_val

        if winner:
            p1_stack.append(p1_val)
            p1_stack.append(p2_val)
        else:
            p2_stack.append(p2_val)
            p2_stack.append(p1_val)

    if len(p1_stack) != 0:
        return True

    return False

def main():
    in_file = open('input.txt', 'r')
    player2 = False
    p1_stack = list()
    p2_stack = list()

    for in_line in in_file:
        if in_line == 'Player 1:\n':
            continue

        if in_line == 'Player 2:\n':
            player2 = True
            continue

        if in_line == '\n':
            continue

        if player2:
            p2_stack.append(int(in_line))
        else:
            p1_stack.append(int(in_line))

    combat(p1_stack, p2_stack)

    if len(p1_stack) != 0:
        winning_stack = p1_stack
    else:
        winning_stack = p2_stack

    score_idx = 0
    score = 0

    for card in winning_stack:
        score = score + card * (len(winning_stack) - score_idx)
        score_idx = score_idx + 1

    print(score)

main()
