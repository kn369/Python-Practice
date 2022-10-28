# Repetition structures exerxise 2  QUESTION 1

number=int(input('Enter the first number in the series :'))
Sum=0

while number > 0 :
    Sum=Sum + number
    number=int(input('Enter the next number in the series :'))

print('Sum of all the numbers is ',Sum)
