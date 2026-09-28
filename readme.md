# Expense Tracker

1. Project Overview

Expense Tracker is a basic Python project made to keep track of personal expenses.

The idea behind this project is simple. Instead of writing expenses down somewhere separately, the user can enter them into the program and store them in a CSV file. The user can then view the saved expenses, find the total amount spent, or search for expenses using a category.

I made this project to apply the basic Python concepts covered in the course to a small real-world problem. The project mainly focuses on functions, file handling, CSV operations, loops, conditions, modules, and input validation.

2. Problem Statement

Keeping track of small daily expenses can become difficult when they are recorded in different places or not recorded at all.

The purpose of this project is to provide a simple command-line interface where a user can:

Add an expense

Store the expense details

View previously added expenses

Calculate total spending

Search for expenses based on category

The project uses a CSV file for storing the data, so a separate database is not required.

3. Objectives

The main objectives of this project are:

To create a simple system for recording expenses.

To store expense information in a structured format.

To calculate the total amount spent.

To allow expenses to be searched by category.

To practice Python file handling and CSV operations.

To divide the program into separate modules instead of putting everything in one file.

To handle basic invalid input.

4. Features

### Add Expense

The user can enter the name, amount, and category of an expense. The details are then saved in the CSV file.

### View Expenses

The user can view all the expenses that have been stored so far.

### Calculate Total

The program reads the expense amounts from the CSV file and calculates the total spending.

### Search by Category

The user can enter a category such as Food, Travel, or Education and see the expenses belonging to that category.

### Input Validation

The amount entered by the user is checked so that it is greater than zero. Invalid numerical input is also handled.

5. Technologies Used

The project is built using:

Python 3.14

CSV

File Handling

OS module

Command Line Interface (CLI)

Git and GitHub for version control

No external Python packages are required for the current version of the project.

6. Project Structure

```text
Expense-Tracker/

│

├── main.py

├── expense_operations.py

├── analytics.py

├── file_manager.py

├── input_utils.py

├── expense.csv

└── README.md
```

### main.py

This is the main program file. It provides the menu and controls the overall flow of the application.

The available options are:

1. Add Expense

2. View Expenses

3. Calculate Total

4. Search by Category

5. Exit

### expense_operations.py

This file contains functions related to adding and displaying expenses.

### analytics.py

This file contains the functions used to calculate total spending and search expenses by category.

### file_manager.py

This file checks whether the CSV file exists. If it does not exist, it creates the file and adds the required headings.

### input_utils.py

This file is used for checking the amount entered by the user and handling invalid input.

### expense.csv

This is the data file where the expense records are stored.

7. How the Program Works

The basic workflow of the project is:

```text
Start

↓

Check/Create CSV File

↓

Display Main Menu

↓

User Selects an Option

↓

┌─────────────────────────────┐

│ 1. Add Expense              │

│ 2. View Expenses            │

│ 3. Calculate Total          │

│ 4. Search by Category       │

│ 5. Exit                     │

└─────────────────────────────┘

↓

Perform Selected Operation

↓

Return to Main Menu

↓

Exit
```

The program continues to show the menu until the user selects the exit option.

8. Data Storage

The project uses a CSV file instead of a database.

The file contains three main fields:

Name,Amount,Category

For example:

Lunch,150,Food

Bus Ticket,30,Travel

Notebook,80,Education

This approach keeps the project simple and is suitable for a basic Python project.

9. Requirements

Before running the project, make sure that Python 3.14 is installed.

To check the Python version:

```bash
python --version
```

On Windows, you can also use:

```bash
py --version
```

No additional libraries need to be installed.

## 10. How to Run the Project

Step 1: Download or Clone the Repository

Clone the project using Git:

```bash
git clone <https://github.com/avinash-chandna/Expense-Tracker>
```

Then open the project folder:

```bash
cd Expense-Tracker
```

Step 2: Run the Program

Use:

```bash
python main.py
```

If you are using Windows and the above command does not work, try:

```bash
py main.py
```

Step 3: Use the Menu

After starting the program, the following menu will appear:

===== EXPENSE TRACKER =====

1. Add Expense

2. View Expenses

3. Calculate Total

4. Search by Category

5. Exit

Enter your choice:

Select the option according to what you want to do.

## 11. Example

### Adding an Expense

Enter expense name: Lunch

Enter amount: 150

Enter category: Food

Expense added successfully!

### Viewing Expenses

===== EXPENSES =====

Name: Lunch | Amount: ₹150 | Category: Food

Name: Bus Ticket | Amount: ₹30 | Category: Travel

### Calculating Total

Total Expenses: ₹180.00

### Searching by Category

Enter category to search: Food

===== SEARCH RESULTS =====

Name: Lunch | Amount: ₹150 | Category: Food

## 12. Testing

The project can be tested manually by running the program and checking each menu option.

Test 1: Add Expense

Input:

Name: Lunch

Amount: 150

Category: Food

Expected result:

The expense should be added to expense.csv.

Test 2: View Expenses

Action:

Select option 2.

Expected result:

Previously stored expenses should be displayed.

Test 3: Calculate Total

Action:

Select option 3.

Expected result:

The program should add the amounts of all stored expenses and display the total.

Test 4: Search Category

Action:

Enter an existing category such as Food.

Expected result:

Expenses belonging to that category should be displayed.

Test 5: Invalid Amount

Input:

-50

Expected result:

Amount must be greater than zero.

The program should ask for the amount again.

Test 6: Invalid Menu Choice

Input:

8

Expected result:

The program should display an invalid-choice message and show the menu again.

## 13. Error Handling

Basic error handling has been included in the project.

For example, while entering an amount, the program checks whether the input is a valid number. It also checks that the amount is greater than zero.

This prevents simple input mistakes from stopping the program.

## 14. Non-Functional Requirements

The project also has some basic non-functional requirements:

Usability

The program uses a simple menu so that a user can select an operation without needing complicated commands.

Reliability

Expense information is stored in a CSV file so that it remains available after the program is closed.

Maintainability

The code is divided into different Python files according to their purpose. This makes individual parts of the program easier to understand and modify.

Error Handling

The program checks invalid amounts and invalid menu choices instead of immediately terminating.

## 15. Limitations

There are some limitations in the current version:

It is a command-line application.

Data is stored in a CSV file rather than a database.

There is no login or user management.

Expenses cannot currently be edited or deleted.

There are no graphs or visual reports.

The project is mainly designed for basic expense tracking.

These limitations also provide possibilities for improving the project in the future.

## 16. Future Enhancements

Some features that can be added in future versions are:

Add date and time to every expense.

Add edit and delete options.

Add monthly and yearly expense reports.

Add a budget feature.

Add charts for different expense categories.

Use SQLite for better data management.

Add a graphical user interface.

Add income tracking.

Add export options for reports.

## 17. What I Learned

While working on this project, I got practical experience with:

Creating and calling functions

Using loops and conditional statements

Reading and writing files

Working with CSV data

Using Python modules

Handling invalid user input

Separating a program into multiple files

Using Git and GitHub to manage a project

The project helped me understand how basic Python concepts can be combined to solve a small real-world problem.

## 18. Conclusion

The Expense Tracker is a simple Python project for recording and managing daily expenses.

Although the project is basic, it covers several important Python concepts and shows how they can be used together to create a working application. The current version focuses on keeping the implementation simple and understandable, while leaving room for additional features in the future.

## 19. Repository

The complete source code and project files are available in this GitHub repository:

< https://github.com/avinash-chandna/Expense-Tracker>

## 20. Author

Name: Avinash Chandna
Course: B.Tech CSE Core
University: VIT Bhopal University
Project: Expense Tracker
