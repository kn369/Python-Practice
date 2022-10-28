last_number=6
for row in range (1,last_number):
    for column in range (1,row +1):
        print(column,end='')
    print("")


last_number=5
for row in range (last_number,-1,-1):
    for column in range (1,row):
        print(column,end='')
    print("")
