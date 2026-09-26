import csv
import os

file_name = "expense.csv"

def setup_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Amount", "Category"])