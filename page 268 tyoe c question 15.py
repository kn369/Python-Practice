#page 268 type c question 15

respond="yes"
list=[]

while respond=="yes":
    y=int(input("enter the number : "))
    list.append(y)
    respond=input("Do you want to add more numbers? Type yes if you want to: ")

print(max(list))
