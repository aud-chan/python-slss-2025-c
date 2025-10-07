# (String) methods
# Author: Audrey
# 6 October 2025

# Ask the user what the weather is like
weather = input("What's the weather like today?")

    # Rainy, RAINY, RAiny
    # Rainy!
    # Rainy.
if weather.lower().strip("!.,? ") == "rainy":
    print("You should bring an umbrella.")
else:
    print("I see...")
