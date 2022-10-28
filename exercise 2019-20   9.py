# PROGRAMMING EXERCISES 9

income=int(input("Enter your monthly income"))

def tax(I):
    state_sales_tax=(5/100)*income
    country_sales_tax=(25/1000)*income
    print("Your state sales tax is ",state_sales_tax,"$ and country sales tax is ",country_sales_tax,"$")

tax(income)
