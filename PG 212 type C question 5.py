#type c page 212 question 5

year=int(input("Enter year: "))
y=year%4
x=year%100
z=year%400

((y==0 and x!=0 and z!=0) or (y==0 and x==0 and z==0)  and print("It is a leap year")) or ((y!=0 or (x==0 or z==0)) and print("it is not a leap year"))


      
