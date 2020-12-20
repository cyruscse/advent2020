# Advent of Code 2020 Day 18 Part 1 solution
# Cyrus Sadeghi

def parse_vals(equation, result):
    ret_early = 0

    while '(' in result:
        result = parse_vals(equation, result[1:])

        if type(result) is list:
            ret_early = result[1]
            result = result[0]

    if len(equation) == 0:
        return result

    oper = equation.pop(0)

    ret_early = equation[0].count(')')
    val2 = equation.pop(0).strip(')')

    while '(' in val2:
        val2 = parse_vals(equation, val2[1:])

        if type(val2) is list:
            ret_early = val2[1]
            val2 = val2[0]

    result = int(result)
    val2 = int(val2)

    if oper == '*':
        result = result * val2
    else:
        result = result + val2

    result = str(result)

    if ret_early > 0:
        return [result, ret_early - 1]

    return parse_vals(equation, result)

def main():
    equations = open('input.txt', 'r')
    hw_sum = 0

    for equation in equations:
        equation = equation.strip().split()
        result = 0

        hw_sum = hw_sum + int(parse_vals(equation, equation.pop(0)))

    print(hw_sum)

main()
