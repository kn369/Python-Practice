# chapter 4 exercise 6

hours=float(input('Enter hours:'))
rate=float(input('Enter rate:'))

def computepay(hours,rate):
    if hours>40:
        over_time=hours-40
        x=((1/2)*rate)*over_time
        y=rate*hours
        pay=x+y
        print('pay:',pay)
    else:
        pay=hours*rate
        print('pay:',pay)

computepay(hours,rate)
        
