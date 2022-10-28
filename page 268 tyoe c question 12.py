#page 268 type c question 12

side_1=float(input("Enter side of triangle: "))
side_2=float(input("Enter side of triangle: "))
side_3=float(input("Enter side of triangle: "))

if side_1==side_2==side_3:
    print("It is a equilateral triangle")
elif side_1==side_2 or side_2==side_3 or side_1==side_3:
    print("It is a isoseles triangle")
else:
    print("It is a scalene triangle")
