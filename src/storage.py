import os
import csv
from datetime import datetime 
from utilities import fin_summary

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir=os.path.join(base_dir,"data")
data_file=os.path.join(data_dir,"transaction.csv") ## To make sure csv file from data folder only is used
report_dir='reports'

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

def ensure_rep():
    # Creating report directory if not exists
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

def export_csv(fin_summary,cat_summary):
    ensure_rep()

    transactions=load_transaction(data_file)

    today=datetime.now().strftime("%d-%m-%Y")
    filename=f"{report_dir}/expense_report_{today}.csv"
 
    expense=fin_summary[0]
    income=fin_summary[1]
    balance=income-expense

    with open (filename,"w") as f:
        #HEADING
        writer=csv.writer(f)
        writer.writerow(["REPORT"])
        writer.writerow([today])
        writer.writerow([])

        #SUMMARY
        writer.writerow(["SUMMARY"])
        writer.writerow([f"Total Income",income])
        writer.writerow([f"Total Expense",expense])
        writer.writerow([f"Balance",balance])
        writer.writerow([])

        #CATEGORY WISE SUMMARY
        writer.writerow(["Category","Amount"])

        for category,amount in cat_summary.items():
            writer.writerow([category,amount])

        writer.writerow([])

        #TRANSACTIONS
        writer.writerow(["TRANSACTIONS"])
        writer.writerow(["Date","Amount","Type","Category","Description"])
        for txn in transactions:
            writer.writerow([
                txn["Date"],
                txn["Amount"],
                txn["Type"],
                txn["Category"],
                txn["Description"]
            ])
    return filename

def export_txt(fin_summary,cat_summary):
    ensure_rep()

    transactions=load_transaction(data_file)

    today=datetime.now().strftime("%d-%m-%Y")
    filename=f"{report_dir}/expense_report_{today}.txt"

    expense=fin_summary[0]
    income=fin_summary[1]
    balance=income-expense


    with open(filename,'w') as f:
        f.write("----- EXPENSE TRACKER REPORT -----\n")
        f.write(f"Generated on {today}\n")
        f.write("\n")

        #SUMMARY
        f.write("----- SUMMARY -----\\n")
        f.write(f"Total Income:{income}\n")
        f.write(f"Total Expense:{expense}\n")
        f.write(f"Balance:{balance}\n")
        f.write("\n")    

        #CATEGORY WISE SUMMARY
        f.write("----- CATEGORY WISE SUMMAR -----\n")
        f.write("Category:Amount\n")

        for category,amount in cat_summary.items():
            f.write(f"{category}:{amount}")
            f.write("\n")
        
        #TRANSACTIONS
        f.write("----- ALL TRANSACTIONS -----")
        f.write("Date | Amount | Type | Category | Description\n")
        for txn in transactions:
            line=(
                f"{txn["Date"]} | "
                f"{txn["Amount"]} | "
                f"{txn["Type"]} | "
                f"{txn["Category"]} | "
                f"{txn["Description"]}\n"
            )
            f.write(line)
    return filename