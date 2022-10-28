# chapter 4 exercise 7


marks=float(input('Enter your score:'))

def computegrade(marks):
    if marks >= 0.9:
        print('A')
    
    elif marks >= 0.8:
        print('B')
    
    elif marks >= 0.7:
        print('C')

    elif marks >= 0.6:
        print('D')

    else:
        print('F')

computegrade(marks)
