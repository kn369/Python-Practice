A=int(input('Enter the month number:'))

if A in [1,3,5,7,8,10,12]:
    print('Month has 31 days')
elif A==2:
    print('Month has 28 days')
else:
    print('Month has 30 days')
    
