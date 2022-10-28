#This program tells wether the color of the pocket is green, black or red

n=int(input('Enter any integeral pocket number ::'))

if n==0:
    print('pocket color is green')

elif n>=1 and n<=10:
    if n%2==0:
        print('pocket color is black')
    else:
        print('pocket color is red')

elif n>=11 and n<=18:
    if n%2==0:
        print('pocket color is red')
    else:
        print('pocket color is black')

elif n>=19 and n<=28:
    if n%2==0:
        print('pocket color is black')
    else:
        print('pocket color is red')

elif n>=29 and n<=36:
    if n%2==0:
        print('pocket color is red')
    else:
        print('pocket color is black')

else:
    print('Error')
