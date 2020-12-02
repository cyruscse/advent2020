def find_numbers(expenses):	
    for expense1 in expenses:
        for expense2 in expenses:
            if expense1 + expense2 == 2020:
                return [expense1, expense2]

def main():
    expenses = open('input.txt', 'r')
    expense_list = list()

    for expense in expenses:
        expense_list.append(int(expense))

    numbers = find_numbers(expense_list)

    print(numbers[0] * numbers[1])

main() 