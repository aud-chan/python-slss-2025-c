# Maths Stuff
# Author : Audrey
# 12 November 2025

# Do math things in python

# import math
# side_length = float(input("side length"))
# hypotenuse = float(input("hypotenuse length"))
# angle_degrees = math.asin(side_length/hypotenuse)
# print(f"The degree of the angle is {angle_degrees}")

# Find the average price of plane tickets
def ticket_price():
    numbers = [
        "Price for first search: ",
        "Price for second search: ",
        "Price for third search: ",
    ]
    for number in numbers:
        total = 0
        print(numbers)
        pricing = float(input(f"Amount: ").strip("!?,. "))
        total += pricing
        average = total/len(numbers)
        print(f"the average price for this trip is: {average}")

    numbers2 = [
        "Price for first search:"
        "Price for second search: ",
        "Price for third search:",
    ]







def main():
    ticket_price()

if __name__ == "__main__":
    main()
