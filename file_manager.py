import csv
import os

expense_file = "expense.csv"

def setup_file():
    if not os.path.exists(expense_file):
        with open(expense_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Amount", "Category"])