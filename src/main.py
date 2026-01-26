import logging as lg
from storage import initialize_storage,save_transaction, load_transaction,data_file
from storage import del_transac
from utilities import valid_category,valid_type,fin_summary,cat_summary

lg.basicConfig(
    filename="expense_tracker.log",
    level=lg.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

transactions=load_transaction(data_file)


def add_transaction():
    while True:
            d=input("Enter the date of transaction (DD-MM-YY): ")
            a=int(input("Enter amount (₹): "))
            t=valid_type()
            c=valid_category()
            des=input("Description of expense: ")
            save_transaction(d,a,t,c,des)
            print("Transaction saved successfully")
            i=input("'Add' or 'Quit': ")
            if i=="Quit":
                break

def display_transactions(transactions):
    print("-"*80)
    print(f"{'Date':<12}{'Amount':<10}{'Type':<12}{'Category':<12}{'Description':}")
    print("-"*80)

    for i, t in enumerate(transactions,start=1):
        print(
            f"{i:<3}"
            f"{t['Date']:<12}"
            f"{t['Amount']:<10}"
            f"{t['Type']:<8}"
            f"{t['Category']:<10}"
            f"{t['Description']}"
        )
    print("-"*80)

def show_summary():
    transactions=load_transaction(data_file)
    if not transactions:
        print("No Transactions found.")

    expense,income=fin_summary(transactions)
    balance=income-expense
    print("---------- FINANCIAL SUMMARY ----------")
    print(f"Total Income : Rs. {income}")
    print(f"Totala Expense : Rs. {expense}")
    print(f"Net Balance : Rs. {balance}")

def categ_summary():
    transactions=load_transaction(data_file)
    summary=cat_summary(transactions)
    print("---------- EXPENSE BY CATEGORY ----------")
    for category,amount in summary.items():
        print(f"{category:<15} Rs. {amount:.2f}")
    
initialize_storage()


while True:
    print("==============================")
    print("   EXPENSE TRACKER SYSTEM")
    print("==============================")
    print('1. Add new transaction \n 2. View all transactions \n 3. View monthly summary \n 4. View category-wise summary \n 5. Delete a transaction\n 6. Export report\n 7. Exit')
    choice=int(input("Enter your choice: "))
    if (choice==7):
        break
    elif (choice==1):
        add_transaction()
    elif (choice==2):
        for t in transactions:
            print(type(t),t)
        display_transactions(transactions)
    elif(choice==3):
        show_summary()
    elif(choice==4):
        categ_summary()
    elif(choice==5):
        if not transactions:
            print("No Transactions available to delete")
            continue
        display_transactions(transactions)
        
        index=int(input("Enter transaction index to delete(0=Cancel deletion): "))
        if index==0:
            print("Canceled the deletion process..\n Thank You..")
            continue
        success=del_transac(index-1)
        
        if success:
            print("Transaction deleted successfully")
            transactions=load_transaction(data_file)
        else:
            print("Invalid transaction index")

    else:
        lg.WARNING(f"Invalid menu choice entered: {choice}")
        print('Invalid choice. Please choose from 1-7')
       