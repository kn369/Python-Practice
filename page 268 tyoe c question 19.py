#page 268 type c question 19

n=int(input("Enter the value of n: "))
m=int(input("Enter the value of m: "))

for x in range(1,n+1):
    if x%m==0:
        if x%2==0:
            print(x,"-->even")
        else:
            print(x,"-->odd")
