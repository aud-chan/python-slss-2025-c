# Functions
# Author: Audrey
# 8 October 2025

# function to print "hello" to the console
def say_hello():
    print("hello")

# function to print a personalized hello
def say_hello_personal(name= "Tiger"):
    print(f"hello{name}!")


def normalized_input():
	# get input from the user
	output = input()
	# .strip and .lower the input
	output = output.strip(",?! ").lower()
	# return the ouput
	return output

# Ask the user for the weather
print("What's the weather like?")
weather_reply = normalized_input()

if weather_reply == "rainy":
	print("You should bring an umbrealla.")


def some_fun():
    print("hello!")
    return None

def some_fun_return() -> str:
    print("hello!")
    return "purple monkey dishwasher!"

return_val = some_fun_return()
print(return_val)

say_hello_personal("David") # David is the argument
say_hello_personal()
