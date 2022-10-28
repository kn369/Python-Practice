A=str(input('Enter any character:'))

if A>='a' and A<='z' or A>='A' and A<='Z':
    print('Character is alphabet')
elif A>="0" and A<="9":
    print('Character is digit')
else:
    print('Character is a special character')
