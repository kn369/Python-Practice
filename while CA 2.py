# This program asks the user to enter any positive integer and find its factorial

n=int(input('Enter any positive integer :'))
x=1
total=1

while x<=n:
    print(x)
    total=total*x
    x=x+1
print('Total=',total)
