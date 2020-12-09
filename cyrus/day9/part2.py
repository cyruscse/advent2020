# Advent of Code 2020 Day 9 Part 2 solution
# Cyrus Sadeghi

def main():
    numbers = open('input.txt', 'r')
    preamble = list()
    bad_number = 0

    for number in numbers:
        found_pair = False
        intnum = int(number)

        if (len(preamble) < 25):
            preamble.append(intnum)
        else:
            for val in preamble:
                if intnum > val and (intnum / 2 != val) and (intnum - val) in preamble:
                    found_pair = True
                    break

            if found_pair == False:
                bad_number = intnum
                break
            else:
                del preamble[0]
                preamble.append(intnum)

    numbers = open('input.txt', 'r')
    preamble = list()

    for number in numbers:
        intnum = int(number)
        sum = 0

        for val in preamble:
            sum = sum + val

        if sum < bad_number:
            preamble.append(intnum)
        elif sum == bad_number:
            print(min(preamble) + max(preamble))
            return
        else:
            while sum > bad_number:
                sum = sum - preamble[0]
                del preamble[0]

            if sum == bad_number:
                print(min(preamble) + max(preamble))
                return

            preamble.append(intnum)

main()