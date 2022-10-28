
def main():
    value=float(input("Enter the value of your property: "))
    assessment(value)

def assessment(a):
    assessment=a*0.60
    print("Your assessment value is ",assessment)
    tax(assessment)

def tax(b):
    a=b/1000
    tax=a*7.2
    print("Your tax is ",tax)

main()
