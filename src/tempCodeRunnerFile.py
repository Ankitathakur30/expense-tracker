
    with open ('transaction.csv','a') as f:
        f.write('Date,Amount,Type,Category,Description')

def save_transaction(d,a,t,c,des):
    with open ('transaction.csv','a') as f:
        f.write(f'{d},{a},{t},{c},{des}')
d=input("Enter the date of transaction: ")
a=int(input("Enter amount: "))
t=input("Expense/Income")
c=input("Category of expense(Food/Travel/Others/None): ")
des=input("Description of expense: ")
initialize_storage()
save_transaction(d,a,t,c,des)
#def load_transaction():12