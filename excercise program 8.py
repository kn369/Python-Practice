

 
n=9
last_number=6
for row in range (last_number,-1,-1):
    for column in range (1,row):
        if column < row-1:
            print(' ',end='')
        else:
            print('*',end='')
           
    print("")
