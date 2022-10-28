#This program calculates percentage of a student in 80M exam

Name=input('Please enter your full name :') 
marks1=float(input('Enter your marks of Social Science :'))
marks2=float(input('Enter your marks of Science :'))
marks3=float(input('Enter your marks of Mathematics :'))
marks4=float(input('Enter your marks of English :'))
marks5=float(input('Enter your marks of Gujarati or Hindi :'))
percentage=(marks1+marks2+marks3+marks4+marks5)/400*100
print('',Name,'you have achieved ',percentage,'%')
