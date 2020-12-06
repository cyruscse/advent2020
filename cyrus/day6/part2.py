# Advent of Code 2020 Day 6 Part 2 solution
# Cyrus Sadeghi

def group_end(yes, group_answers):
    group_common = group_answers[0]
    for group_answer in group_answers:
        if len(group_answer) == 0:
            break
        group_common = group_common.intersection(group_answer)
    return yes + len(group_common)

def main():
    answers = open('input.txt', 'r')
    yes = 0
    group_answers = list()
    single_answers = set()

    for line in answers:
        for char in line:
            if char == '\n':
                continue
            single_answers.add(char)

        group_answers.append(single_answers)
        single_answers = set()

        if line[0] == '\n':
            yes = group_end(yes, group_answers)
            group_answers = list()
            continue

    print(group_end(yes, group_answers))

main()