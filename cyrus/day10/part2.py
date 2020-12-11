# Advent of Code 2020 Day 10 Part 2 solution
# Cyrus Sadeghi

def main():
    adapter_file = open('input.txt', 'r')
    adapters = list()
    potentials = dict()
    idx = 0
    jolts = 0
    max_adapter = 0
    values = dict()

    adapters.append(0)

    for adapter in adapter_file:
        adapters.append(int(adapter))

    adapters = sorted(adapters)

    while idx < len(adapters):
        jolt_poss = list()

        if adapters[idx] + 1 in adapters:
            jolt_poss.append(adapters[idx] + 1)
        if adapters[idx] + 2 in adapters:
            jolt_poss.append(adapters[idx] + 2)
        if adapters[idx] + 3 in adapters:
            jolt_poss.append(adapters[idx] + 3)

        potentials[adapters[idx]] = jolt_poss
        max_adapter = adapters[idx]
        idx = idx + 1

    adapters = sorted(adapters, reverse = True)
    values[max_adapter] = 1

    for adapter in adapters:
        if adapter == max_adapter:
            continue

        values[adapter] = 0

        for value in potentials[adapter]:
            values[adapter] = values[adapter] + values[value]

    print(values[0])

main()