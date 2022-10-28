# This program prints shipping charges of any package

w=int(input('Enter weight of your package ::'))

if w<=2:
    print('Your shipping charge is $1.50')

elif w>2 and w<=6:
    print('Your shipping charge is $3.00')

elif w<10 and w>6:
    print('Your shipping charge is $4.00')

if w>=10:
    print('Your shipping charge is $4.75')
