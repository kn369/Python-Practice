
x=int(input('Enter any natural number:'))
f=1
F=0
while f <= x:
    if x%f==0:
        print(f)
        F=F+1
    f=f+1
print('No. of factors are ',F)

if F<3:
    print(x,'is prime number')
elif F==1:
    print(x,'is niether prime nor composite number')
else:
    print(x,'is composite number')
