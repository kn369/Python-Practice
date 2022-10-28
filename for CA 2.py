#This program computes the factorial of number n given by user

n=int(input('Enter any natural number:'))
p=1

for n in range (1,n+1,1):
    p=p*n
print(p)
