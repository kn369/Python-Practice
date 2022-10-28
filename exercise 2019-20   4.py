# EXERCISE 2029-20 QUESTION 4

Loan_payment=int(input('Enter your monthly costs :'))
Insurance=int(input('Enter your monthly costs :'))
Gas=int(input('Enter your monthly costs :'))
Oil=int(input('Enter your monthly costs :'))
Tyre=int(input('Enter your monthly costs :'))
Maintainance=int(input('Enter your monthly costs :'))

def MonthlyCost_AnnualCost(a,b,c,d,e,f):
    monthly_cost=Loan_payment + Insurance + Gas + Oil + Tyre + Maintainance
    print("Your monthly cost is ",monthly_cost)
    annual_cost= 12*monthly_cost
    print("Your annual cost is ",annual_cost)

MonthlyCost_AnnualCost(Loan_payment,Insurance,Gas,Oil,Tyre,Maintainance)


