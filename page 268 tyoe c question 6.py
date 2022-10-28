#page 268 type c question 6

side_1=float(input("Enter the first side: "))
side_2=float(input("Enter the second side: "))
side_3=float(input("Enter the third side: "))

if side_1+side_2>side_3 and side_2+side_3>side_1 and side_3+side_1>side_2:
      print("Triangle is possible")
else:
      print("Triangle is not possible")
      
      
