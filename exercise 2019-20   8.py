# PROGRAMMING EXERCISES 8

area=int(input("Enter the square feet of area to be painted :"))
cost=int(input("Enter the cost of paint per gallon :"))

def account(A,C):
    gallons=area/112
    hours=(8/112)*area
    cost_of_paint=gallons*cost
    labor_charges=35.00*hours
    TotalCost=gallons+hours+cost_of_paint+labor_charges

    print("Gallons of paint required is ",gallons,"gallons")
    print("The hours of labor required is ",hours,"hours")
    print("The cost of the paint is ",cost_of_paint,"$")
    print("The labor charges are ",labor_charges,"$")
    print("The total cost of this job will be ",TotalCost,"$")

account(area,cost)
