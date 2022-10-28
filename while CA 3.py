#This program calculates sum of every third number from 1 to 1001

x=1
total=0
while x<=1001 :
    print(x)
    total=total+x
    x=x+3
print('total=',total)
