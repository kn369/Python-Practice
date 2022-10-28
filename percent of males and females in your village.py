#this program calculates percentage of males and females in village


males=int(input('Enter the number of males living in your village :'))
females=int(input('Enter the number of females living in your village :'))
Total=males+females
percent_of_males=males/Total*100
percent_of_females=females/Total*100
print('Percent of females living in your village is ',percent_of_females,'%')
print('Percent of males living in your village is ',percent_of_males,'%')
