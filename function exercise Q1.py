
def main():
    miles=float(input("Enter the distance in miles: "))
    converter(miles)

def converter(miles):
    kilometer=miles/0.6214
    print("The distance in kilometers is ",kilometer)

main()
