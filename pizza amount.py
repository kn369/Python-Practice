#This program calculates GST and total amount to be paid

price_pizza1=float(input('Type the amount of 1st pizza'))
price_pizza2=float(input('Type the amount of 2nd pizza'))
price_pizza3=float(input('Type the amount of 3rd pizza'))
price_pizza4=float(input('Type the amount of 4th pizza'))
price_pizza5=float(input('Type the amount of 5th pizza'))
subtotal=price_pizza1+price_pizza2+price_pizza3+price_pizza4+price_pizza5
GST=9/100*subtotal
total_amount=GST+subtotal                   
print('You have purchased pizzas of Rs ',subtotal)
print('GST on your purchase is Rs ',GST)
print('You have to pay Rs ',total_amount,"including all taxes")
                   
