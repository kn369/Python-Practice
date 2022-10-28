#page 256 type c question 11

x="yes"
num=0
N=0
while x=="yes":
      n=int(input("enter number: "))
      N=N+n
      x=input("do you want to add more numbers? type yes if you want to: ")
      num=num+1

average=N/(num)
print(average)
