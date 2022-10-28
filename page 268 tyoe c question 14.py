#page 258 type c question 14

N=int(input("Enter the number N>20: "))

for x in range(11,N+1):
    print(x)

if N%21==0:
    print("Tipsy Topsy")
elif N%3==0:
    print("Topsy")
elif N%7==0:
    print("Tipsy")
else:
    print("N is not divisible by 7 or 3!")
    
