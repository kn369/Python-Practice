
sales_list=[]
def sales( ):
    for x in range (1,8):
        store_sales=int(input("Enter the sales of the day :" ))
        sales_list.append(store_sales)
    Total_sales=0
    for x in range (7):
        Total_sales=Total_sales+sales_list[x]    
        
    print(Total_sales ,"is the total sales of the week ")
    print(sales_list)
sales( )

