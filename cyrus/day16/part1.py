# Advent of Code 2020 Day 16 Part 1 solution
# Cyrus Sadeghi

def main():
    ticket_input = open('input.txt', 'r')
    stage = 0
    valid_values = set()
    my_values = list()
    other_values = list()

    for line in ticket_input:
        if line[0] == '\n':
            stage = stage + 1
            continue

        line = line.strip()

        if stage == 0:
            spl = line.split(':')[1].strip().split(' or ')

            for entry in spl:
                max_value = int(entry.split('-')[1])
                min_value = int(entry.split('-')[0])

                idx = min_value

                while idx - 1 != max_value:
                    valid_values.add(idx)
                    idx = idx + 1
        elif stage == 1:
            if 'ticket' in line:
                continue

            vals = line.split(',')
            for val in vals:
                my_values.append(int(val))
        else:
            if 'ticket' in line:
                continue

            vals = line.split(',')
            ticket = list()
            for val in vals:
                ticket.append(int(val))
            other_values.append(ticket)

    error_rate = 0

    for ticket in other_values:
        for val in ticket:
            if val not in valid_values:
                error_rate = error_rate + val

    print(error_rate)

main() 