#Repetition structures exercise 2 QUESTION 3

n=int(input('Enter any nonnegative ineger:'))
x=1

for n in range (1,n+1,1):
    x=x*n
    n=n
    print(n,'Factorial is',x)


