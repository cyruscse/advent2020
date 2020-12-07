# Advent of Code 2020 Day 7 Part 2 solution
# Cyrus Sadeghi

import re

def count_bags(key, mapping):
    if 'no other' in mapping[key][0]:
        return 0

    sum = 0

    for nested in mapping[key]:
        sum = sum + int(nested[1]) + (int(nested[1]) * count_bags(nested[0], mapping))

    return sum

def main():
    rules = open('input.txt', 'r')
    comp_result = re.compile("[^\W\d]")
    mapping = dict()
    holds_gold = 0

    for rule in rules:
        split_rule = rule.split('contain')
        key = split_rule[0].split('bags')[0].strip()
        values = list()

        for contains in split_rule[1].split(','):
            split_str = contains.split('bag')[0]
            search_res = comp_result.search(split_str)
            bag_count = [split_str[search_res.start():].strip(), split_str[:search_res.start()].strip()]
            values.append(bag_count)

        mapping[key] = values

    print(count_bags('shiny gold', mapping))

main()