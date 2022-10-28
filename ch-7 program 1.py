store_sales_Monday=int(input("Enter the store sales for Monday :"))
store_sales_Tuesday=int(input("Enter the store sales for Tuesday :"))
store_sales_Wednesday=int(input("Enter the store sales for Wednesday :"))
store_sales_Thursday=int(input("Enter the store sales for Thursday :"))
store_sales_Friday=int(input("Enter the store sales for Friday :"))
store_sales_Saturday=int(input("Enter the store sales for Saturday :"))
store_sales_Sunday=int(input("Enter the store sales for Sunday :"))

list_store_sales=[store_sales_Monday,store_sales_Tuesday,store_sales_Wednesday,store_sales_Thursday,store_sales_Friday,store_sales_Saturday,store_sales_Sunday]

Total_sales=0
for x in range (7):
    Total_sales=Total_sales+list_store_sales[x]
    
print("The total sales for the week is ",Total_sales)
    