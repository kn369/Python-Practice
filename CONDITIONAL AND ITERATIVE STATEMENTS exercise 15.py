for row in range (7):
    for column in range (7):  
        if row == 0 or row == 6:
            print('#' , end='  ')
        elif row == column and column< 5:
            print ('#' , end='  ')
        elif (row ==5 and column==6):
             print ('#' , end='  ')
        else:
            print('  ' , end='  ')
    print('  ')
    
