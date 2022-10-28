# A=p(1+r/n)**nT
# I=prT/100

p=float(input('Enter your principal:'))
r=float(input('Enter your rate:'))
R=float(input('Enter your increase time in years:'))
T=float(input('Enter your time in years:'))
I=p*r*T/100
n=R/12
A=p*(1+r/n)**(n*T)
print('Your SI is Rs',I,'and amount is Rs',A)
