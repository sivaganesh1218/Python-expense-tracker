
expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            for expense in expenses:
                print(expense)

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Expenses: ₹", total)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
