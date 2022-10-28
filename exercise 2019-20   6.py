# PROGRAMMING EXERCISES 6

Fat_grams=int(input("Enter fat grams :"))
Carb_grams=int(input("Enter carb grams :"))

def nutrition_chart (a,b):
    calories_from_fat=Fat_grams*9
    calories_from_carb=Carb_grams*4
    print("Calories obtained from fat are ",calories_from_fat)
    print("Calories obtained from carb are ",calories_from_carb)

nutrition_chart(Fat_grams,Carb_grams)
