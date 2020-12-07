# Advent of Code 2020 Day 7 Part 1 solution
# Cyrus Sadeghi

import re

def hold_gold(key, mapping):
    if 'no other' in mapping[key]:
        return False

    if 'shiny gold' in mapping[key]:
        return True

    for nested in mapping[key]:
        if hold_gold(nested, mapping) == True:
            return True

    return False

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
            values.append(split_str[search_res.start():].strip())

        mapping[key] = values

    for key in mapping.keys():
        if hold_gold(key, mapping):
            holds_gold = holds_gold + 1

    print(holds_gold)

main()