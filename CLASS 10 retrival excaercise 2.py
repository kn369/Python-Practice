# This program prints discount and amount to be paid for 'Q' number of packages purchased 

Q=int(input('Enter number of packages purchased ::'))

if Q>=10 and Q<=19:
    amount=(90/100)*(99*Q)
    discount = (10/100)*(99*Q)
    print('Amount of purchase is ',amount,'including discount of ',discount)

elif Q>=20 and Q<=49:
    amount=(80/100)*(99*Q)
    discount = (20/100)*(99*Q)
    print('Amount of purchase is ',amount,'including discount of ',discount)

elif Q>=50 and Q<=99:
    amount=(70/100)*(99*Q)
    discount = (30/100)*(99*Q)
    print('Amount of purchase is ',amount,'including discount of ',discount)

elif Q>=100:
    amount=(60/100)*(99*Q)
    discount = (40/100)*(99*Q)
    print('Amount of purchase is ',amount,'including discount of ',discount)

else:
    amount=(99*Q)
    print('Amount of purchase is ',amount)
