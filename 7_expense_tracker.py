total_expense = 0


def add_expense(amount):
    global total_expense
    total_expense += amount
    print(f"Added expense: {amount}. Total expenses: {total_expense}")


def get_expense():
    return total_expense


def main():
    while True:
        print("\nChoose an action:")
        print("1. Add an expense")
        print("2. View the total amount of expenses")
        print("3. Exit")

        choice = input("\nYour choice ( 1 | 2 | 3 ): ")

        match choice:
            case "1":
                try:
                    amount = float(input("\nEnter the expense amount: "))
                    if amount < 0:
                        print("The expense cannot be negative!")
                    else:
                        add_expense(amount)
                except ValueError:
                    print("Please enter a valid number.")

            case "2":
                total = get_expense()
                print(f"The total amount of expenses: {total}")

            case "3":
                print("Thank you. Have a nice day!")
                break

            case _:
                print("Incorrect choice, please try again.")


main()
