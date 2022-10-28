#page 260 type c question 20(a)

n=1
Sn=0
for x in range(7):
    if n%2==0:
        numerator=-(2+x*3)
        denominator=(9+x*4)
    else:
        numerator=(2+x*3)
        denominator=(9+x*4)
    
    Sn=numerator/denominator+Sn
    n=n+1
    print(numerator/denominator)
print(Sn)
