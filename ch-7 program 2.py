January=int(input("Enter the total rainfall in January :"))
February=int(input("Enter the total rainfall in February :"))
March=int(input("Enter the total rainfall in March :"))
April=int(input("Enter the total rainfall in April :"))
May=int(input("Enter the total rainfall in May :"))
June=int(input("Enter the total rainfall in June :"))
July=int(input("Enter the total rainfall in July :"))
August=int(input("Enter the total rainfall in August :"))
September=int(input("Enter the total rainfall in September :"))
October=int(input("Enter the total rainfall in October :"))
November=int(input("Enter the total rainfall in November :"))
December=int(input("Enter the total rainfall in December :"))

Months_list=[January,February,March,April,May,June,July,August,September,October,November,December]

Rainfall=0
for x in range (12):
   Rainfall=Rainfall+Months_list[x]
   
Average=Rainfall/12
print("Average rainfall of this year is ",Average)

print(max(Months_list))


