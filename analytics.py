import csv
from file_manager import file_name
def total_expenses():
    total = 0.0
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[1])
    print(f"\nTotal Spending: ₹{total:.2f}")

def search_by_category(target_category):
    found = False
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)
        
        print(f"\n===== RESULTS FOR: {target_category.upper()} =====")
        for row in reader:
            if row[2].lower() == target_category.lower():
                print(f"Name: {row[0]} | Amount: ₹{row[1]}")
                found = True
    if not found:
        print("No expenses found in this category.")