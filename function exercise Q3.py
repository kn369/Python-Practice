
def main():
    cost=float(input("Enter the replacement cost of your property: "))
    minimum_insurance(cost)

def minimum_insurance(cost):
    insurance=0.08*cost
    print("You must take minimum insurance of ",insurance)

main()
