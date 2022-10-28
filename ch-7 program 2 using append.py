
my_list=['January','February','March','April','May','June','July','August','September','October','November','December']
rainfall_list=[]

def rainfall( ):
    for x in range (12):
        rain=int(input("Enter the total rainfall of the month :" ))
        rainfall_list.append(rain)
    
    average_rainfall=0
    for x in range (12):
        average_rainfall=average_rainfall+rainfall_list[x]  
    
    average=average_rainfall/12
    print(average ,"is the average rainfall of the month ")
    print(rainfall_list)
    
    for y in range (12):
        if rainfall_list[y]==max(rainfall_list):
            print(my_list[y], 'has greatest rainfall')
            
        if rainfall_list[y]==min(rainfall_list):
            print(my_list[y], 'has lowest rainfall')        
    
rainfall( )

