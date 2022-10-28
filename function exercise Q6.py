
def main():
    fat_grams=float(input("Enter the amount of fat grams you had: "))
    carb_grams=float(input("Enter the amount of carb grams you had: "))
    fat_cal(fat_grams)
    carb_cal(carb_grams)

def fat_cal(a):
    fats=a*9
    print("You had ",fats,"calories of fats")

def carb_cal(a):
    carbs=a*4
    print("You had ",carbs,"calories of carbs")


main()
    
