# PROGRAMMING EXERCISES 7

Class_A=int(input("Enter the number of tickets booked in class A"))
Class_B=int(input("Enter the number of tickets booked in class B"))
Class_C=int(input("Enter the number of tickets booked in class C"))

def amount(A,B,C):
    Amount=(Class_A*20)+(Class_B*15)+(Class_C*10)
    print('Total amount to be paid is ',Amount,'$')

amount(Class_A,Class_B,Class_C)
