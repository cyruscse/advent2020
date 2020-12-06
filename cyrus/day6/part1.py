# Advent of Code 2020 Day 6 Part 1 solution
# Cyrus Sadeghi

def main():
    answers = open('input.txt', 'r')
    yes = 0
    group_answers = set()

    for line in answers:
        if line[0] == '\n':
            group_answers = set()
            continue

        for char in line:
            if char == '\n':
                continue
            if char not in group_answers:
                yes = yes + 1
            group_answers.add(char)

    print(yes)

main()