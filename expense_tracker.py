import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Initialize file with headers if not exists
def initialize_file():
    try:
        with open(FILE_NAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date"])
    except FileExistsError:
        pass

# Add expense
def add_expense():
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, date])

        print(" Expense added successfully!\n")

    except ValueError:
        print(" Invalid amount!\n")

# View all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            print("\n--- All Expenses ---")
            for row in reader:
                print(f"Amount: {row[0]}, Category: {row[1]}, Date: {row[2]}")
            print()

    except FileNotFoundError:
        print("No expenses found.\n")

# Total expense
def total_expense():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                total += float(row[0])

        print(f"\n Total Expense: {total}\n")

    except:
        print("Error calculating total.\n")

# Category-wise summary
def category_summary():
    summary = {}

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                category = row[1]
                amount = float(row[0])

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        print("\n Category Summary:")
        for cat, amt in summary.items():
            print(f"{cat}: {amt}")
        print()

    except:
        print("Error reading data.\n")

# Main menu
def main():
    initialize_file()

    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()

  




    