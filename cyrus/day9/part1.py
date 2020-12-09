# Advent of Code 2020 Day 9 Part 1 solution
# Cyrus Sadeghi

def main():
    numbers = open('input.txt', 'r')
    preamble = list()

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
                print(intnum)
                return
            else:
                del preamble[0]
                preamble.append(intnum)

main()