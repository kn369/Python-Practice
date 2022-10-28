# chapter 4 exercise 3 (2)

num=int(input('Input a number'))
times=2
y=1
for product in range(num,num*10+1,num):
    for n in range(times):
        y=y+1
    times=times+1
        
    print(num,'*',n,'=',product)
        

        
    
        
