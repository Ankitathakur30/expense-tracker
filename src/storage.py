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
        f.write(f'{d},{a},{t},{c},{des}\n')
        
def load_transaction(data_file):
    transactions=[]
    with open(data_file,'r',newline="") as f:
        reader=csv.DictReader(f)
        for row in reader:
            transactions.append(row)
    return transactions

def del_transac(index):
    
    with open(data_file,"r") as f:
        reader=csv.DictReader(f)
        transactions=list(reader)
        fieldnames=reader.fieldnames
        
    if index<0 or index>len(transactions):
        print("Invalid Index !!!")
        return False 

    transactions.pop(index) #Remove the seleced transaction

    #Rewrite CSV with remaining data
    with open(data_file,"w") as f:
        writer=csv.DictWriter(f,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
    return True
