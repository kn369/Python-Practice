#page 268 type c question 17

respond="yes"
list=[]

while respond=="yes":
    y=(input("enter the number : "))
    list.append(y)
    respond=input("Do you want to add more numbers? Type yes if you want to: ")

list.reverse()
if list==list.reverse():
    print("It is a palindrome!!")
else:
    print("It is not a palindrome")
