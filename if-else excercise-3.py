# This program recieves 2 no. and operator from user and computes it

x=float(input('Enter first number'))
y=float(input('Enter second number'))
z=input('Enter any arithematic operator')

if z=='+':
    a=x+y
if z=='-':
    a=x-y
if z=='*':
    a=x*y
if z=='/':
    a=x/y
print(a,'is greatest number')
