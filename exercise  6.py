string_list=[]
again="y"

while again == "y":
    num=input("Enter the number in the list :")
    string_list.append(num)
    
    again=input("Do yo want to add word ? "
                "(y= yes and any other character means no) :")
seperator="-"
print(seperator.join(string_list))
    
    
