# McDoBot
# Author: Audrey
# 6 October 2025
# Write a McDonald's bot that asks if you want fries with your meal.
# Call it work-mcdobot.py
# It should accept Yes/yes or No/no as inputs, and reply appropriately depending on the answer.
# If the user inputs anything else, it should repeat back their answerand say that it does not understand.


fries = input("Would you like fries with your meal?")

if fries.lower().strip("!.,? ") == "yes":
    print("Here's your meal with fries!")
elif fries.lower().strip("!?,. ") == "no":
    print("Here's your meal without fries.")
else:
    print(f"Sorry, I don't understand {fries}")
