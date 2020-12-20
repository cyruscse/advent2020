# Advent of Code 2020 Day 19 Part 1 solution
# Cyrus Sadeghi

import copy

def validate_rule(rules, message, rule_idx):
    rule_list = rules[rule_idx]

    if type(rule_list[0]) is list:
        for nrule_list in rule_list:
            for nrules in nrule_list:
                msg_copy = copy.deepcopy(message)
                passed = True

                for nrule in nrules:
                    msg_copy = validate_rule(rules, msg_copy, nrule)
                    if msg_copy == None:
                        passed = False
                        break

                if passed == True:
                    message = copy.deepcopy(msg_copy)
                    return message

        return None

    elif type(rule_list[0]) is str:
        if message[0] == rule_list[0]:
            del message[0]
            return message
        else:
            return None
    elif type(rule_list[0]) is int:
        msg_copy = copy.deepcopy(message)

        for rule in rule_list:
            msg_copy = validate_rule(rules, msg_copy, rule)

            if msg_copy == None:
                return None

        return msg_copy

def main():
    rules_messsages = open('input.txt', 'r')
    rules = dict()
    messages = list()
    good_messages = 0

    for line in rules_messsages:
        if ':' in line:
            rule_num = int(line.split()[0].strip(':'))
            sline = line.split()
            sline.pop(0)

            if '\"' in line:
                rules[rule_num] = sline[0].strip('\"')
            else:
                limits = list()
                idx = 1

                if '|' in line:
                    limits1 = list()
                    limits2 = list()
                    stage = 0

                    for val in sline:
                        if val == '|':
                            stage = stage + 1
                            continue

                        if stage == 0:
                            limits1.append(int(val))
                        else:
                            limits2.append(int(val))

                    limits.append([limits1, limits2])
                else:
                    for val in sline:
                        limits.append(int(val))

                rules[rule_num] = limits
        elif len(line) == 1:
            continue
        else:
            messages.append(list(line.strip()))


    for message in messages:
        output = validate_rule(rules, message, 0)
        if type(output) is list and len(output) == 0:
            good_messages = good_messages + 1

    print(good_messages)

main()
