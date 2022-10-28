import turtle
turtle.color("black")
turtle.speed(10)

length=int(input("Enter the length of the rectangle: "))
breadth=int(input("Enter the breadth of the rectangle: "))

def square(x):
    for s in range(2): 
        turtle.fd(length+100*x)
        turtle.rt(90)
        turtle.fd(breadth+100*x)
        turtle.rt(90)

def diagonal(x):
    if x<2:
        turtle.lt(135)
        turtle.fd((5000)**(1/2))
        turtle.rt(135)
def main():   
    for x in range(3):
        if x==0:
            turtle.begin_fill()
        square(x)
        turtle.end_fill()
        diagonal(x)
    side(1,0)
        
def side(x,y):
    turtle.penup()
    turtle.goto(length*x,breadth*y)
main()
turtle.pendown()
turtle.goto(length+100,100)
side(0,-1)
turtle.pendown()
turtle.goto(-100,-breadth-100)
side(1,-1)
turtle.pendown()
turtle.goto(length+100,-breadth-100)

def edge(x,y):
    turtle.penup()
    turtle.goto((length/2)*x,(breadth/2)*y)
    turtle.pendown()
    
edge(1,0)     
turtle.lt(90)
turtle.fd(100)
edge(0,-1)
turtle.lt(90)
turtle.fd(100)
edge(2,-1)
turtle.lt(180)
turtle.fd(100)
edge(1,-2)
turtle.rt(90)
turtle.fd(100)


