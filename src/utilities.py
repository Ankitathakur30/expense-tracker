def valid_type():
    while True:
        t=input("Income/Expense: ").lower()
        if t=="income" or t=="expense":
            break
        else:
            print("Invalid Input!!!\nPlease enter again.")
    return t
def valid_category():
    while True:
        c=input("Category of expense(Food/Travel/Bill/Groceries/Others/None): ").lower()
        if c=="food" or c=="travel"or c=="bill" or c=="groceries" or c=="others" or c=="none":
            break
        else:
            print("Invalid input !!!\nPlease enter again.")
    return c
def fin_summary(transactions):
    total_income=0
    total_expense=0
    for t in transactions:
        amount=float(t['Amount'])
        if t['Type'].lower()=='income':
            total_income=total_income+amount
        elif t['Type'].lower()=='expense':
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