# Advent of Code 2020 Day 19 Part 2 solution
# Cyrus Sadeghi

def parse_rule(rule_str):
    rule_idx = rule_str.strip().split(':')[0]
    rule_str = rule_str.strip().split(':')[1][1:].strip('\"')

    return (rule_idx, rule_str)

def test_rule(rules, rule_idx, sequence, sequence_idx):
    #if len(sequence) == sequence_idx + 1:
        ##print('ereturn')
        #return False

    offset = 0
    retval = False
    sub_rule_list_idx = 0

    for sub_rule_list in rules[rule_idx]:
        #print('testing {} with {}'.format(sub_rule_list, sequence[(sequence_idx + offset):]))
        if str(sub_rule_list[0]).isalpha():
            if sequence_idx >= len(sequence):
                return True
            #print('{} {}'.format(sequence, sequence_idx))
            return (str(sub_rule_list[0]) == sequence[sequence_idx])
        sub_rule_list_failed = False
        for sub_rule in sub_rule_list:
            #print('{} {}'.format(sub_rule, offset))
            #if len(sequence) == sequence_idx + offset + 1:
                #if sub_rule_list_idx == len(rules[rule_idx]):
                    ##print('eol')
                    #return False
                #break

            retval = test_rule(rules, sub_rule, sequence, sequence_idx + offset)
            #print('{} returned {}'.format(sub_rule, retval))

            if retval == False:
                if sub_rule_list_idx == (len(rules[rule_idx]) - 1):
                    #print('greturn')
                    return False
                sub_rule_list_failed = True
                break

            offset = offset + retval
            #print('increment {}'.format(sequence[(offset + sequence_idx):]))

        if sub_rule_list_failed == False:
            #print('sub list {} passed'.format(sub_rule_list))
            return offset
        else:
            offset = 0

        #if sub_rule_idx == len(sub_rule_list):
            ##print('freturn {} {} {} {} {}'.format(sub_rule_idx, sub_rule_list, rule_idx, offset, len(sequence)))
            #if rule_idx == 0:
                #return (offset == (len(sequence)))
            #return offset

        sub_rule_list_idx = sub_rule_list_idx + 1

    #print('final return {} {} {}'.format(rule_idx, sequence_idx, offset))
    return offset

def main():
    in_file = open('part2input.txt', 'r')
    rules = dict()
    inputs = list()
    reading_inputs = False
    good_inputs = 0

    for in_line in in_file:
        if in_line == '\n':
            reading_inputs = True
            continue

        if reading_inputs:
            inputs.append(in_line.strip())
        else:
            parsed = parse_rule(in_line)
            sub_rules = parsed[1].split('| ')
            parsed_list = list()

            for sub_rule in sub_rules:
                parsed_sub_list = list()
                for element in sub_rule.split(' '):
                    if element == '':
                        continue
                    if element.strip().isdigit():
                        stripped_element = int(element.strip())
                    else:
                        stripped_element = element.strip()
                    parsed_sub_list.append(stripped_element)
                parsed_list.append(parsed_sub_list)

            rules[int(parsed[0])] = parsed_list

    for sequence in inputs:
        #print('testing {}'.format(sequence))
        final_offset = test_rule(rules, 0, sequence, 0)
        
        if final_offset == len(sequence):
            good_inputs = good_inputs + 1

    print(good_inputs)

main()
