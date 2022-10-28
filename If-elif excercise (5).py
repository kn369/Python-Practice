A=float(input('Enter first side of triangle'))
B=float(input('Enter second side of triangle'))
C=float(input('Enter third side of triangle'))
if A>0 and B>0 and C>0 and A+B>C and A+C>B and B+C>A:
    if A==B and B==C:
        print('Equilateral triangle')
    elif A==B or B==C or C==A:
        print('Isosceles triangle')
    else:
        print('Scalene triangle')
    
