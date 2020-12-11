# Advent of Code 2020 Day 10 Part 1 solution
# Cyrus Sadeghi

def main():
    adapter_file = open('input.txt', 'r')
    adapters = list()
    one_jolt = 0
    three_jolt = 0
    current_jolt = 0

    for adapter in adapter_file:
        adapters.append(int(adapter))

    while len(adapters) != 0:
        saved_jolt = current_jolt
        high_jolt = 0

        for adapter in adapters:
            if adapter - current_jolt == 3:
                high_jolt = adapter
            elif adapter - current_jolt == 1:
                current_jolt = adapter
                one_jolt = one_jolt + 1
                break

        if current_jolt == saved_jolt:
            current_jolt = high_jolt
            three_jolt = three_jolt + 1

        adapters.remove(current_jolt)

    three_jolt = three_jolt + 1

    print(three_jolt * one_jolt)

main()