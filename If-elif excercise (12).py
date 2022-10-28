a=int(input('Enter the marks of Maths subject:'))
b=int(input('Enter the marks of Science subject:'))
c=int(input('Enter the marks of Social Science subject:'))
d=int(input('Enter the marks of English subject:'))
e=int(input('Enter the marks of Hindi subject:'))

p=(a+b+c+d+e)/5

if p>90:
    print('Grade A')
elif 80<=p and p<=90:
    print('Grade B')
elif 70<=p and p<80:
    print('Grade C')
elif 60<=p and p<70:
    print('Grade D')
elif 40<=p and p<60:
    print('Grade E')
else:
     print('Grade F')
