#page 258 type c question 8

num=int(input("Enter a number: "))
root=num**(1/2)
if num==1:
    print("it's neither prime nor composite")
for f in range(2,half):
    if root%f==0:
        print("It is not a prime number")
        break 
elif num==1:
    print("It is neither prime number nor composite")
else:
    print("it is a prime number")
    
        
