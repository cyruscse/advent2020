# Advent of Code 2020 Day 8 Part 1 solution
# Cyrus Sadeghi

def main():
    program = open('input.txt', 'r')
    program_lines = program.readlines()
    encountered_lines = set()
    idx = 0
    accumulator = 0

    while idx < len(program_lines) - 1:
        instruction = program_lines[idx].split(' ')[0]
        value = int(program_lines[idx].split(' ')[1].strip())

        if idx in encountered_lines:
            print(accumulator)
            return

        encountered_lines.add(idx)

        if instruction == 'acc':
            accumulator = accumulator + value
            idx = idx + 1
        elif instruction == 'jmp':
            idx = idx + value
        elif instruction == 'nop':
            idx = idx + 1

main()