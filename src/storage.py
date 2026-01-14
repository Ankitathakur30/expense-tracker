import os
import csv
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir=os.path.join(base_dir,"data")
data_file=os.path.join(data_dir,"transaction.csv") ## To make sure csv file from data folder only is used

def initialize_storage():
    if not os.path.exists(data_file) or os.path.getsize(data_file)==0:
        with open(data_file,'w') as f:
            f.write('Date,Amount,Type,Category,Description\n')

def save_transaction(d,a,t,c,des):
    with open(data_file,'a') as f:
        f.write(f'{d},{a},{t},{c},{des}')
d=input("Enter the date of transaction: ")
a=int(input("Enter amount: "))
t=input("Expense/Income: ")
c=input("Category of expense(Food/Travel/Others/None): ")
des=input("Description of expense: ")
initialize_storage()
save_transaction(d,a,t,c,des)
def load_transaction(data_file):
    with open(data_file,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            print(f"Date:{row['Date']},\n Amount:{row['Amount']},\nType:{row['Type']},\nCategory:{row['Category']},\nDescription:{row['Description']}")
load_transaction(data_file)