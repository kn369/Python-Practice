A=float(input('Enter first angle of a triangle:'))
B=float(input('Enter second angle of a triangle:'))
C=float(input('Enter third angle of a triangle:'))

if A>0 and B>0 and C>0 and A+B+C==180:
    print('Triangle is valid')
else:
    print('Triangle is not valid')
