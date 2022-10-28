
for row in range (4):
    n=8
    for column in range (row+1):
        if column == 0:
            print(n , end='  ')
        else:
            print(n-2*column, end='  ')
    print('  ')
