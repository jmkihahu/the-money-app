import time,os

#odk

listas = [] 

os.system("cls")

def write():
        print()
        print('Creating a new file')

        name = input('Enter a name for your file: ').strip().lower()+'.txt'  # Name of text file coerced with +.txt

        try:
            with open(name,"w") as file:# Trying to create a new file or open one
                for row in listas:
                    file.write(f"{row['name']} :: {row['money']}\n")
            print(f"Data saved to {name}")
            exit()
        except Exception as e:
            print(f"Something went wrong! {e}")
 
def preety_print():
    print("\n Current entries :")
    if not listas:
        print("\t No Entries")
    for row in listas:
        for key,value in row.items():
            print(f"\t\t {key} :: {value:^10}")




def entry():
    entry = True
    while entry:
        time.sleep(1)
        print("\t\t === Add Name ===")
        print()

        name_1 = input("Enter your name : ").strip().lower()
        money_1 = float(input("enter money : ").strip())

        product = {"name":name_1 , "money":money_1}
        listas.append(product)    

        add = input("Would you like to add more[y/n]: ").strip().lower()
        if add != "yes" or add[0] != "y":
            entry = False



def add_money():
    time.sleep(2)
    preety_print()
    print("\t\t === Add Money === ")
    print()
    name_2 = input("enter your name:").strip().lower()
    for row in listas:
        if row["name"] == name_2:
            money_2 =  float(input("How much money would you like to add : "))
            row["money"] += money_2
            time.sleep(1)
            print()
            print(f"money updated for \033[4m {name_2.title()} \033[0m ")
            return
    print("Name not found")

def subtract_money():
    time.sleep(1)
    print()
    preety_print()
    print()
    
    print("\t\t === Subtract Money === ")

    name_2 = input("enter your name: ").strip().lower()
    for row in listas:
        if row["name"] == name_2:
            money_2 =  float(input("How much money would you like to subtract : "))
        
            if money_2 > row["money"]:
                print("Cannot subtract more than current balance")
                return            
            row["money"] -= money_2
            time.sleep(1)
            print()
            print(f"money updated for \033[4m {name_2.title()} \033[0m ")
            return
    print("Name not found")


def main():
    while True:
        time.sleep(2)
        print("""
              ==== MENU ====
                1. Add Name : 
                2. Add  money:
                3.Subtract money:
                4.Show entries
                5.Quit
              """)
        choice = int(input("Enter either [1-5]:\n  "))
        if choice == 1 :
            entry()

        elif choice == 2 :
            add_money()

        elif choice == 3:
            subtract_money()
        
        elif choice == 4:
            preety_print()

        elif choice == 5:
            leave = input("Are you sure you would like to quit: ")
            if leave[0] == "y" or leave == "yes":
                write()
                
        else:
            print("Invalid choice. Please try again")
                        
main()

