import csv
import os
File = "expense.csv"
def create_file():
    if not os.path.exists(File):
        with open(File, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Amount", "Category"])
def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    with open(File, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])

    print("Expense added successfully!")
def view_expenses():
    with open(File, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n===== EXPENSES =====")

        for row in reader:
            print(f"Name: {row[0]} | Amount: ₹{row[1]} | Category: {row[2]}")
def calculate_total():
    total = 0
    with open(File, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[1])
    print(f"\nTotal Expenses: ₹{total:.2f}")
def search_category():
    category = input("Enter category to search: ")

    found = False

    with open(File, "r") as file:
        reader = csv.reader(file)

        next(reader)

        print("\n===== SEARCH RESULTS =====")

        for row in reader:
            if row[2].lower() == category.lower():
                print(f"Name: {row[0]} | Amount: ₹{row[1]} | Category: {row[2]}")
                found = True

    if not found:
        print("No expenses found in this category.")
        
create_file()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Search by Category")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        calculate_total()

    elif choice == "4":
        search_category()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")