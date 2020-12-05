# Advent of Code 2020 Day 5 Part 1 solution
# Cyrus Sadeghi


def main():
    seat_ids = open('input.txt', 'r')
    max_seat_id = 0

    for seat_id in seat_ids:
        min_row_num = 0
        max_row_num = 127
        row_num = 0
        min_col_num = 0
        max_col_num = 7
        col_num = 0

        for half in seat_id:
            if half == 'F':
                row_num = max_row_num = max_row_num - ((max_row_num - min_row_num + 1) / 2)
            elif half == 'B':
                row_num = min_row_num = min_row_num + ((max_row_num - min_row_num + 1) / 2)
            elif half == 'R':
                col_num = min_col_num = min_col_num + ((max_col_num - min_col_num + 1) / 2)
            elif half == 'L':
                col_num = max_col_num = max_col_num - ((max_col_num - min_col_num + 1) / 2)

        if (row_num * 8 + col_num) > max_seat_id:
            max_seat_id = row_num * 8 + col_num

    print(max_seat_id)

main()