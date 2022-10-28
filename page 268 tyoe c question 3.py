hour=int(input("enter an hour between 1 to 12: "))
hours_ahead=int(input("enter numbers of hours ahead: "))
x=hour + hours_ahead
(x>12 and print("Time is ",x-12,"o clock")) or (x<=12 and print("Time is ",x,"o clock"))




