#page 268 type c question 16

respond="yes"
list=[]
n=0

while respond=="yes":
    y=int(input("enter the number : "))
    list.append(y)
    n=n+1
    respond=input("Do you want to add more numbers? Type yes if you want to: ")

x=-1*n
list.sort()
seq=list[0:n-1]
print(max(seq))
