#This is a number guessing game
from random import*

x = randint(0,100)                  #decide on the random number

# give user instructions
print("Welcome to number guessing game!")
print("You have to guess the correct number in 5 tries.")
print("The number is from 0 to 100.")
print("All The Best!")

# taking input from the user
for a in range(5):
    num = int(input("Enter your guess: "))
    if x==num:
        print("WooHoo! You got it!")
        break
    elif num<x:
        print("The number entered is lower.")
    else:
        print("The number entered is higher.")
    print("You have ",4-a," attemps remaining.")

print("You failed to guess the correct number ")
print("The correct number was ",x)