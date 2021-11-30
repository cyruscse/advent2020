# Advent of Code 2020 Day 25 Part 1 solution
# Cyrus Sadeghi

def calculate_pubkey(value, subject):
    value = value * subject
    value = value % 20201227
    return value

def main():
    in_file = open('input.txt', 'r')
    doorpubkey = 0
    cardpubkey = 0

    for line in in_file:
        if doorpubkey == 0:
            doorpubkey = int(line)
        else:
            cardpubkey = int(line)
            break

    guessdoorpubkey = 1
    doorloop = 0

    while guessdoorpubkey != doorpubkey:
        guessdoorpubkey = calculate_pubkey(guessdoorpubkey, 7)
        doorloop = doorloop + 1

    guesscardpubkey = 1
    cardloop = 0

    while guesscardpubkey != cardpubkey:
        guesscardpubkey = calculate_pubkey(guesscardpubkey, 7)
        cardloop = cardloop + 1

    privatekeyloop = 0
    encryptionkey = 1

    while privatekeyloop != doorloop:
        encryptionkey = calculate_pubkey(encryptionkey, cardpubkey)
        privatekeyloop = privatekeyloop + 1

    print(encryptionkey)

    '''
    verification
    privatekeyloop = 0
    encryptionkey = 1

    while privatekeyloop != cardloop:
        encryptionkey = calculate_pubkey(encryptionkey, doorpubkey)
        privatekeyloop = privatekeyloop + 1

    print(encryptionkey)
    '''

main()