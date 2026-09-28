# Project Statement – Expense Tracker

## 1. Problem Statement

Managing daily expenses is something people do regularly, but it can be easy to lose track of where money is being spent. Small expenses such as food, travel, stationery, and other daily purchases can add up over time.

For this project, I wanted to make a simple program that keeps expense details in one place. Instead of maintaining expenses manually, the user can enter the details into the program and save them in a CSV file.

The project is a basic command-line Python application. It allows the user to add expenses, view previously entered expenses, calculate the total amount spent, and search for expenses by category.

The main purpose of making this project is to apply the Python concepts learned in the course to a practical problem.

## 2. Scope of the Project

The current project focuses on basic personal expense tracking.

The user can enter three details for an expense:

- Expense name
- Amount
- Category

These details are stored in a CSV file named `expense.csv`.

The project currently covers:

- Adding new expenses
- Viewing stored expenses
- Calculating total expenses
- Searching for expenses by category
- Basic input validation
- Storing data using a CSV file

The scope has been kept simple because the main goal is to understand and demonstrate basic Python programming and file-handling concepts.

## 3. Limitations

The current version of the project has a few limitations:

- It is a command-line application and does not have a graphical interface.
- Expense data is stored in a CSV file instead of a database.
- Expenses cannot currently be edited or deleted after being added.
- The project does not provide advanced reports or charts for analyzing expenses.

These features can be considered for future improvements as the project is developed further.

## 4. Target Users

The project is mainly intended for people who want a simple way to keep track of their everyday expenses.

Possible users include:

- Students who want to keep track of their daily spending
- Individuals who want a simple personal expense record
- Beginners who want to understand how a basic expense-management program works

The application is especially suitable for users who are comfortable using a simple terminal-based program.

## 5. High-Level Features

### 5.1 Add Expense

The user can enter the name, amount, and category of an expense. The information is then stored in the CSV file.

### 5.2 View Expenses

The user can view all the expenses that have been recorded so far.

### 5.3 Calculate Total

The program reads the stored expenses and calculates the total amount spent.

### 5.4 Search by Category

The user can search for expenses using a category such as `Food`, `Travel`, or `Education`.

### 5.5 Basic Input Validation

The program checks the amount entered by the user. Amounts less than or equal to zero are not accepted, and invalid numerical input is handled.

## 6. Expected Outcome

The expected outcome of this project is a small and easy-to-use expense tracking application that works through the command line.

By completing this project, I aim to demonstrate that I can use basic Python concepts to create a working solution for a real-world problem. The project also gives me practice with file handling, CSV data, functions, modules, loops, conditions, and basic error handling.

## 7. Future Scope

The project can be improved further by adding features such as:

- Editing existing expenses
- Deleting expenses
- Adding the date of an expense
- Setting a monthly budget
- Generating monthly and yearly reports
- Showing expenses using charts
- Moving from CSV storage to a database
- Adding a graphical user interface
- Adding income tracking

These features are outside the scope of the current version but could be considered in future versions.
