# Advent of Code 2020 Day 8 Part 2 solution
# Cyrus Sadeghi

import copy

def fix_attempt(memory, program_lines):
    pair = memory.pop()

    if 'jmp' in program_lines[pair[0]]:
        program_lines[pair[0]] = program_lines[pair[0]].replace('jmp', 'nop')
    elif 'nop' in program_lines[pair[0]]:
        program_lines[pair[0]] = program_lines[pair[0]].replace('nop', 'jmp')

    return pair[0], pair[1], pair[2]

def main():
    program = open('input.txt', 'r')
    program_lines = program.readlines()
    clean_program = copy.deepcopy(program_lines)
    memory = list()
    encountered_indices = set()
    idx = 0
    accumulator = 0
    save_memory = True

    while idx < len(program_lines):
        instruction = program_lines[idx].split(' ')[0]
        value = int(program_lines[idx].split(' ')[1].strip())

        encountered_indices.add(idx)

        if (instruction == 'jmp' or instruction == 'nop') and save_memory == True:
            encountered_indices_copy = copy.deepcopy(encountered_indices)
            memory.append([idx, accumulator, encountered_indices_copy])

        if instruction == 'acc':
            accumulator = accumulator + value
            idx = idx + 1
        elif instruction == 'jmp':
            if idx + value in encountered_indices:
                save_memory = False
                program_lines = copy.deepcopy(clean_program)
                idx, accumulator, encountered_indices = fix_attempt(memory, program_lines)
            else:
                idx = idx + value
        elif instruction == 'nop':
            if idx + 1 in encountered_indices:
                save_memory = False
                program_lines = copy.deepcopy(clean_program)
                idx, accumulator = fix_attempt(memory, program_lines)
            else:
                idx = idx + 1

    print(accumulator)

main()