# Advent of Code 2020 Day 16 Part 2 solution
# Cyrus Sadeghi

import copy

def rec_search(dmr_valid, domains, domain_positions, idx):
    if idx == len(dmr_valid):
        return domain_positions

    domains_copy = copy.deepcopy(domains)

    for domain in dmr_valid[idx]:
        if domain not in domains:
            continue

        domains.remove(domain)
        domain_positions[domain] = idx

        if len(rec_search(dmr_valid, domains, domain_positions, idx + 1)) == 0:
            domains = copy.deepcopy(domains_copy)
            continue

        return domain_positions

    return dict()

def main():
    ticket_input = open('input.txt', 'r')
    my_ticket_stage = False
    domain_ranges = dict()
    my_ticket = list()
    nearby_tickets = list()
    valid_range = set()
    dmr_valid = dict()
    domains = list()

    for line in ticket_input:
        delete_ticket = False

        if 'or' in line.strip():
            domain = line.strip().split(':')[0]
            ranges = line.strip().split(':')[1].strip().split(' or ')
            domain_range = set()

            for rng in ranges:
                min_value = int(rng.split('-')[0])
                max_value = int(rng.split('-')[1])
                idx = min_value

                while idx < (max_value + 1):
                    domain_range.add(idx)
                    valid_range.add(idx)
                    idx = idx + 1

            domain_ranges[domain] = domain_range
            domains.append(domain)
            continue
        if 'your' in line.strip():
            my_ticket_stage = True
        if 'nearby' in line.strip():
            my_ticket_stage = False

        if 'your' in line.strip() or 'nearby' in line.strip() or len(line.strip()) == 0:
            continue

        ticket = list(map(int, line.strip().split(',')))

        if my_ticket_stage == True:
            my_ticket = ticket
        else:
            for value in ticket:
                if value not in valid_range:
                    delete_ticket = True
                    break
            
            if delete_ticket == False:
                nearby_tickets.append(ticket)

    valid_positions = dict()

    for ticket in nearby_tickets:
        idx = 0

        for value in ticket:
            if idx not in valid_positions:
                valid_positions[idx] = set()

            valid_positions[idx].add(value)
            idx = idx + 1

    for domain in domain_ranges.keys():
        for index in valid_positions.keys():
            if len(valid_positions[index]) == len(valid_positions[index].intersection(domain_ranges[domain])):
                if index not in dmr_valid.keys():
                    dmr_valid[index] = set()

                dmr_valid[index].add(domain)

    domain_positions = rec_search(dmr_valid, domains, dict(), 0)
    total = 0

    for domain in domain_positions.keys():
        if 'departure' not in domain:
            continue

        if total == 0:
            total = my_ticket[domain_positions[domain]]
        else:
            total = total * my_ticket[domain_positions[domain]]

    print(total)

main()