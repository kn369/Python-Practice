#This program calculates GST and total amount

amount_of_purchase=float(input('Tell your amount of purchase:'))
GST=9/100*amount_of_purchase
total_cost=amount_of_purchase+GST
print('Your amount of purchase is Rs ',amount_of_purchase)
print("GST on your purchase is Rs ",GST)
print('Your total amount to be paid is Rs ',total_cost)
