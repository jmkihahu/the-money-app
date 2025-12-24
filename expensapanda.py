import pandas as pd
from datetime import datetime

file_name = 'expenses5.csv'



def initialize_file():
    try:
        with open(file_name,'x') as file:
           writer = pd.DataFrame(columns=['Date','Category','Amount','Description'])
           writer.to_csv(file,index=False)
    except FileExistsError:
        pass 

def add_values(): 
    # org_data = []
    # data = pd.read_csv(file_name)
    # org_data.append(data)

    try:
        category = input("Enter the category's name: ").strip().capitalize()
        if not category:
            return
    
        amount = float(input("Enter the amount: ").strip())
        if amount <= 0:
            return
        description = input("Enter a description: ").strip().capitalize()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        og_df = pd.DataFrame({
            'Date':[date],
            'Category':[category],
            'Amount':[amount],
            'Description':[description]
               })

        update_df = pd.read_csv(file_name)
        update_df = pd.concat([update_df, og_df],ignore_index= True)

        update_df.to_csv(file_name,index=False,lineterminator= '\r\n')
    except ValueError:
        print("❌ Invalid input,please try again.")
    print()

def view_expense():
    data = pd.read_csv(file_name)
    data.index +=1
    print (data.head())
    print()

def view_cat_expense():
    data = pd.read_csv(file_name)
    nu = data.groupby('Category')['Amount'].sum()
    grand_totals = nu.sum()
    print()
    print("=== Expenses By Category ===")

    print(f"{'Category':<20} : {'Total':<20} ")
    for category,amt in nu.items():
        print(f'{category:<20} : KES {amt:<20} ')
    
    print()
    print(f"\t\t Grand totals: KES {grand_totals} ")
    print()

def main():
    initialize_file()
    while True:
        print("📑 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Totals")
        print("4. Exit")       
        choice = input("Choose an option: ")
        if choice == '1':
            add_values()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            view_cat_expense() 
        elif choice == '4':
            print("Exiting app")
            break
        else:
            print("❌ Invalid input,please try again.")

main()