# Advent of Code 2020 Day 19 Part 1 solution
# Cyrus Sadeghi

def parse_rule(rule_str):
    rule_idx = rule_str.strip().split(':')[0]
    rule_str = rule_str.strip().split(':')[1][1:].strip('\"')

    return (rule_idx, rule_str)

def test_rule(rules, idx, str):
    if len(str) == 0:
        return (False, str)

    if rules[idx].isalpha():
        return (str[0] == rules[idx], str[1:])

    bkp_str = str
    sub_idx = 0
    sub_rules = rules[idx].split('| ')
    match = False

    for sub_rule in sub_rules:
        sub_rule_ints = sub_rule.strip().split(' ')
        for sub_rule_digit in sub_rule_ints:
            result = test_rule(rules, int(sub_rule_digit), str)

            if result[0] == False:
                str = bkp_str
                match = False
                break
            else:
                str = result[1]
                match = True
            sub_idx = sub_idx + 1
        if match == True:
            break

    return(match, str)

def main():
    in_file = open('input.txt', 'r')
    rules = dict()
    inputs = list()
    reading_inputs = False

    for in_line in in_file:
        if in_line == '\n':
            reading_inputs = True
            continue

        if reading_inputs:
            inputs.append(in_line.strip())
        else:
            parsed = parse_rule(in_line)
            rules[int(parsed[0])] = parsed[1]

    rules_matched = 0

    for input in inputs:
        result = test_rule(rules, 0, input)
        
        if result[0] == True and len(result[1]) == 0:
            rules_matched = rules_matched + 1

    print(rules_matched)

main()
