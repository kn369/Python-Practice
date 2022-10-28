#page 212 type c question 8

num=int(input("Enter the three digit number: "))
hundred=num//100
ten=(num%100)//10
one=num%100-((num%100)//10)*10
NUM=100*one+10*ten+hundred
print(NUM)
