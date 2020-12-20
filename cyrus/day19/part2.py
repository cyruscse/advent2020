# Advent of Code 2020 Day 19 Part 2 solution
# Cyrus Sadeghi

import copy

def validate_rule(rules, message, rule_idx):
    rule_list = rules[rule_idx]
    #print(message)

    if type(rule_list[0]) is list:
        #print('1. checking nested rule list', end = ' ')
        #print(rule_idx)

        for nrule_list in rule_list:
            for nrules in nrule_list:
                msg_copy = copy.deepcopy(message)
                passed = True

                for nrule in nrules:
                    #print('1.x ncheck', end = ' ')
                    #print(nrule)
                    msg_copy = validate_rule(rules, msg_copy, nrule)
                    if msg_copy == None:
                        #print('1.x failed', end = ' ')
                        #print(nrule)
                        passed = False
                        break

                if passed == True:
                    #print('1 passed', end = ' ')
                    #print(rule_idx)
                    message = copy.deepcopy(msg_copy)
                    return message

        return None

    elif type(rule_list[0]) is str:
        #print('2. checking char idx', end = ' ')
        #print(rule_idx)

        if len(message) == 0:
            #print('2. !!! msg empty')
            return None

        if message[0] == rule_list[0]:
            #print('2. char passed', end = ' ')
            #print(rule_idx)
            del message[0]
            return message
        else:
            #print('2. failed', end = ' ')
            #print(rule_idx)
            return None
    elif type(rule_list[0]) is int:
        #print('3. check rule list', end = ' ')
        #print(rule_idx)
        msg_copy = copy.deepcopy(message)

        for rule in rule_list:
            #print('3.x check rule', end = ' ')
            #print(rule)
            msg_copy = validate_rule(rules, msg_copy, rule)

            if msg_copy == None:
                #print('3.x failed', end = ' ')
                #print(rule)
                return None

        #print('3. rule list passed', end = ' ')
        #print(rule_idx)
        return msg_copy

def main():
    rules_messsages = open('input3.txt', 'r')
    rules = dict()
    messages = list()
    good_messages = 0

    for line in rules_messsages:
        if line == "8: 42\n":
            line = "8: 42 | 42 8\n"
        if line == "11: 42 31\n":
            line = "11: 42 31 | 42 11 31\n"

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
                            nlimits = list()
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
        print(message)
        output = validate_rule(rules, message, 0)
        if type(output) is list and len(output) == 0:
            print('good')
            good_messages = good_messages + 1

    #print(good_messages)

main()
