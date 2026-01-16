def valid_type():
    while True:
        t=input("Income/Expense: ")
        if t=="Income":
            break
        elif t=="Expense":
            break 
        else:
            print("Invalid Input!!!\nPlease enter again.")
    return t
def valid_category():
    while True:
        c=input("Category of expense(Food/Travel/Bill/Groceries/Others/None): ")
        if (c=="Food"):
            break
        elif c=="Travel":
            break
        elif c=="Bill":
            break
        elif c=="Groceries":
            break
        elif c=="Others":
            break
        elif c=="None":
            break
        else:
            print("Invalid input !!!\nPlease enter again.")
    return c
def fin_summary(transactions):
    total_income=0
    total_expense=0
    for t in transactions:
        amount=float(t['Amount'])
        if t['Type']=='Income':
            total_income=total_income+amount
        elif t['Type']=='Expense':
            total_expense=total_expense+amount
    return total_expense,total_income

def cat_summary(transactions):
    summary={}
    for t in transactions:
        if t['Type'].lower()=='expense':
            category=t['Category']
            amount=float(t['Amount'])
            summary[category]=summary.get(category,0)+amount
    return summary