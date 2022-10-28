# This program computes and prints that which among the three numbers entered by the user is greatest

x=int(input('Enter number 1:'))
y=int(input('Enter number 2:'))
z=int(input('Enter number 3:'))

if x>=y and x>=z:
    print(x,'is greatest')
elif y>=x and y>=z:
    print(y,'is greatest')
elif z>=y and z>=x:
    print(z,'is greatest')
else:
    print('All are same')
