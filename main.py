
income = 0.0
expenses = {} 

def add_income(amount):
    global income
    if amount > 0:
        income += amount
        print(f"Added ${amount:.2f}")
    else:
        print("Enter positive amount")

def add_expense(category, amount):
    global expenses
    if amount > 0:
        expenses[category] = expenses.get(category, 0) + amount
        print(f"Added {category}: ${amount:.2f}")
    else:
        print("Enter positive amount")

def show_balance():
    total_expenses = sum(expenses.values())
    print(f"Income: ${income:.2f}")
    print(f"Expenses: ${total_expenses:.2f}")
    print(f"Balance: ${income - total_expenses:.2f}")

def main():
    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Exit")
        choice = input("Choose (1-4): ")
        
        if choice == '1':
            try:
                amount = float(input("Income: "))
                add_income(amount)
            except ValueError:
                print("Enter a number")
        elif choice == '2':
            category = input("Category: ")
            try:
                amount = float(input("Amount: "))
                add_expense(category, amount)
            except ValueError:
                print("Enter a number")
        elif choice == '3':
            show_balance()
        elif choice == '4':
            print("Bye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()