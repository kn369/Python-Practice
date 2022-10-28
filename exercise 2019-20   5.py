# EXERCISE 2029-20 QUESTION 5

actual_value=int(input("Enter the actual value of your land :"))

def PropertyTax(a):
    Assessment=0.6*actual_value
    PropertyTax=0.72/100*Assessment
    print("Your property's assessment value is ",Assessment,"and property tax to be paid is ",PropertyTax)


PropertyTax(actual_value)
