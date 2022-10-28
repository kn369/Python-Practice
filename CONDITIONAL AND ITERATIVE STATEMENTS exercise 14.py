
for row in range (7):
    for column in range (7):
        if row == 0 or row==6:
            print ('#' , end='  ')
        elif column == 0 or column == 6:
            print('#' , end='  ')
        else:
            print('  ' , end='  ')
    print('  ')
    print('  ')
