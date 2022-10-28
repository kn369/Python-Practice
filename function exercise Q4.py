
def main():
    loan_payment=float(input("Enter the montly loan payment: "))
    insurance=float(input("Enter the monthly insurance: "))
    gas=float(input("Enter the montly gas cost: "))
    oil=float(input("Enter the montly oil cost: "))
    tires=float(input("Enter the monthly cost spend on tires: "))
    maintenance=float(input("Enter the montly maintenance cost: "))
    monthly(loan_payment,insurance,gas,oil,tires,maintenance)

def monthly(a,b,c,d,e,f):
    monthly_cost=a+b+c+d+e+f
    print("Your monthly cost is ",monthly_cost)
    annual(monthly_cost)

def annual(a):
    annual_cost=a*365
    print("Your annual cost is ",annual_cost)

main()
