# Advent of Code 2020 Day 18 Part 2 solution
# Cyrus Sadeghi

def determine_operators(equation, sidx, eidx):
    operators = list()
    idx = sidx
    offset_ser = 0

    while idx < eidx:
        offset_ser = offset_ser + equation[idx].count('(') - equation[idx].count(')')

        if offset_ser == 0:
            if equation[idx] == '+':
                operators.insert(0, idx)
            elif equation[idx] == '*':
                operators.append(idx)

        idx = idx + 1

    return operators

def parse_vals(equation, sidx, eidx):
    operators = determine_operators(equation, sidx, eidx)
    idx = 0

    while len(operators) != 0:
        oper_idx = operators.pop(0)
        oeqn_len = len(equation)
        val1 = equation[oper_idx - 1]
        oper = equation[oper_idx]
        val2 = equation[oper_idx + 1]

        if ')' in val1:
            neidx = oper_idx - 1
            nsidx = oper_idx - 2
            offset = val1.count(')')

            while offset != 0:
                nsidx = nsidx - 1
                offset = offset - equation[nsidx].count('(') + equation[nsidx].count(')')

            equation[nsidx] = equation[nsidx][1:]
            equation[neidx] = equation[neidx][:-1]

            parse_vals(equation, nsidx, neidx)

            eidx = eidx - (oeqn_len - len(equation))
            operators = determine_operators(equation, sidx, eidx)

            oper_idx = oper_idx - (oeqn_len - len(equation))
            val1 = equation[oper_idx - 1]

        oeqn_len = len(equation)

        if '(' in val2:
            nsidx = oper_idx + 1
            neidx = oper_idx + 1
            offset = val2.count('(')

            while offset != 0:
                neidx = neidx + 1
                offset = offset + equation[neidx].count('(') - equation[neidx].count(')')

            equation[nsidx] = equation[nsidx][1:]
            equation[neidx] = equation[neidx][:-1]
            parse_vals(equation, nsidx, neidx)

            eidx = eidx - (oeqn_len - len(equation))
            operators = determine_operators(equation, sidx, eidx)

            val2 = equation[oper_idx + 1]

        val1 = int(val1)
        val2 = int(val2)

        if oper == '*':
            equation[oper_idx] = str(val1 * val2)
        else:
            equation[oper_idx] = str(val1 + val2)

        del equation[oper_idx + 1]
        del equation[oper_idx - 1]
        eidx = eidx - 2
        operators = determine_operators(equation, sidx, eidx)

    if len(equation) == 1:
        return int(equation[0])

def main():
    equations = open('input.txt', 'r')
    hw_sum = 0

    for equation in equations:
        equation = equation.strip().split()
        result = 0

        hw_sum = hw_sum + int(parse_vals(equation, 0, len(equation) - 1))

    print(hw_sum)

main()
