num_1=float(input("Enter one number: "))
num_2=float(input("Enter second number: "))


d=num_1-num_2
if d<=0.001:
      print("close")
elif d>=-0.01 and d<=0:
      print("close")      
else:
      print("Not close")
      
