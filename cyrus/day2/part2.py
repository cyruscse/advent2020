# Advent of Code 2020 Day 2 Part 2 solution
# Cyrus Sadeghi

def main():
    passwords = open('input.txt', 'r')
    valid_passwords = 0

    for password in passwords:
        pw_entry = password.split()
        pw_restrict = pw_entry[1][0]
        pw_data = pw_entry[2]
        pw_pos_1 = int(pw_entry[0].split('-')[0])
        pw_pos_2 = int(pw_entry[0].split('-')[1])

        pos_1_valid = pw_data[pw_pos_1 - 1] == pw_restrict
        pos_2_valid = pw_data[pw_pos_2 - 1] == pw_restrict

        if (pos_1_valid == True and pos_2_valid == False) or (pos_1_valid == False and pos_2_valid == True):
            valid_passwords = valid_passwords + 1

    print(valid_passwords)

main()