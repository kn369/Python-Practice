A=float(input('Enter the first side :'))
C=float(input('Enter the second side :'))
B=float(input('Enter the third side :'))

if A>0 and B>0 and C>0 and A+B>C and A+C>B and B+C>A:
    print('Triangle is valid')
else:
    print('Triangle is not valid')
    
