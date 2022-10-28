
def main():
    seat_1=int(input("Enter the amount of tickets sold of class A: "))
    seat_2=int(input("Enter the amount of tickets sold of class B: "))
    seat_3=int(input("Enter the amount of tickets sold of class C: "))
    x=class_a(seat_1)
    y=class_b(seat_2)
    z=class_c(seat_3)
    total=x+y+z
    print("The total income generated is ",total)
def class_a(a):
    cost=20*a
    
