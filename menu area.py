      
def main():
    shape=int(input("Enter the shape you want: "))
    if shape==1:
        length=float(input("Enter the length of the rectangle: "))
        breadth=float(input("Enter the breadth of the rectangle: "))
        rectangle(length,breadth)
    elif shape==9 or shape==10:
        length=float(input("Enter the side of the shape: "))
        height=float(input("Enter the height of the shape: "))
        if shape==9:
            paralleogram(length,height)
        else:
            rhombus(length,height)
            
    elif shape==6 or shape==7:
        radius=float(input("Enter the radius of the circle: "))
        if shape==6:
            semi_circle(radius)
        else:
            circle(radius)
    else:
        side=float(input("Enter the side of the shape: "))

    if shape==2:
        pentagon(side)
    elif shape==3:
        hexagon(side)
    elif shape==4:
        heptagon(side)
    elif shape==5:
        octagon(side)
    elif shape==8:
        square(side)
    elif shape==11:
        triangle(side)
        
        
def rectangle(length,breadth):
    area=length*breadth
    print(area)
    
def pentagon(side):
    area=5*(0.375*(side)**2)
    print(area)
    
def hexagon(side):
    area=6*(0.375*(side)**2)
    print(area)
    
def heptagon(side):
    area=7*(0.375*(side)**2)
    print(area)
    
def octagon(side):
    area=8*(0.375*(side)**2)
    print(area)

def semi_circle(radius):
    area=(1/2)*(3.14)*(radius)**2
    print(area)

def circle(radius):
    area=(3.14)*(radius)**2
    print(area)
    
def square(side):
    area=(side)**2
    print(area)

def parallelogram(length,height):
    area=length*height
    print(area)

def rhombus(length,height):
    area=length*height
    print(area)

def triangle():
    area=(0.375)*(side)**2
    print(area)
    
main()









