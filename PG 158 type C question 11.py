#page 158 type c question 11

P=float(input("Enter the principal amount: "))
R=float(input("Enter the rate : "))
T=float(input("Enter the time period: "))
interest=(P*R*T)/100

n=int(input("Enter number of times the amount is compounded per year: "))
compound_interest=P*(1+R/n)**(n*T)-P
print("Interest is ",interest,"compound interest is ",compound_interest)

