
int_list=[]
again="y"
n=0
even_list=[]

while again == "y":
    num=int(input("Enter the number in the list :"))
    int_list.append(num)
    n=n+1
    again=input("Do yo want to add another ? "
                "(y= yes and any other character means no) :")

for x in range (n):
    q =  int_list[x]
    if q%2==0:
        even_list.append(int_list[x])
            
print(max(even_list))

