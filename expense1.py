import csv
from datetime import datetime

File_name = "expenses.csv"

def initialize_file():
    try:
        with open (File_name,"x",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date" , "Category" , "Amount" , "Description"])
    except FileExistsError:
        pass

def add_expense():
    category = input("Enter category (Food,Travel,shopping,etc.) :")
    amount = float(input("Enter amount:"))
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(File_name,"a",newline="" ) as file:
        writer = csv.writer(file)
        writer.writerow ([date, category, amount, description])

        print("✅ Expense added succesfully! \n")

def view_expenses():
    with open (File_name ,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
        print()

def calculate_totals():
    totals = {}
    grand_total = 0
    with open (File_name,"r")as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])
            grand_total += amount
            totals[category] =totals.get(category,0) +amount

            print("\n === Totals by Category ===")
            for cat,total in totals.items():
                print(f'{cat}: KES{total}')
                print(f"Overall total: KES {grand_total} \n")
def edit_expense():
    while True:
        cat1 = input("Enter Category: ").strip().capitalize()
        with open(File_name,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cat = row["Category"]
                if cat1.strip().lower() != cat.strip().lower():
                    print("True")
                    print(f"Found {cat1}")
                    break   
                else:
                    print("Category could not be found,please try again.")
        
        category = input("Enter category:")
        description = input("Enter description:")
        amount = float(input("Enter amount"))
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(File_name,"a") as file:
            writer = csv.writer(file)
            writer.writerow([date , category , description , amount])
            print("Expense edited succesfully ✅")

        rept = input("Would you like to continue editing the list: ").strip().lower()
        if rept == "yes" or rept[0] == "y":
            break
        else:
            continue
            
def main():
    initialize_file()
    while True:
        print("📑 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Totals")
        print("4. Exit")       
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            calculate_totals()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

main()