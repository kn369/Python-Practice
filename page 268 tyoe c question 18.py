#page 268 type c question 18
X=int(input("Enter the number X: "))

n=1
N=0
while n<X:
    n=n*10
    N=N+1
    print(n)
print(X," has ",N,"digits")
Y=N*10+X//(n/10)
print(Y)

