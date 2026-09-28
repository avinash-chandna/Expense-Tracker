import csv
from file_manager import expense_file

def add_new_expense(name, amount, category):
    with open(expense_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])
    print("Expense added successfully!")

def display_all_expenses():
    with open(expense_file, "r") as file:
        reader = csv.reader(file)
        next(reader) 
        
        print("\n===== ALL EXPENSES =====")
        for row in reader:
            print(f"Name: {row[0]} | Amount: ₹{row[1]} | Category: {row[2]}")