# Advent of Code 2020 Day 2 Part 1 solution
# Cyrus Sadeghi

def main():
    passwords = open('input.txt', 'r')
    valid_passwords = 0

    for password in passwords:
        pw_entry = password.split()
        pw_restrict = pw_entry[1][0]
        pw_data = pw_entry[2]
        pw_range_min = int(pw_entry[0].split('-')[0])
        pw_range_max = int(pw_entry[0].split('-')[1])
        
        if pw_data.count(pw_restrict) >= pw_range_min and pw_data.count(pw_restrict) <= pw_range_max:
            valid_passwords = valid_passwords + 1

    print(valid_passwords)

main()