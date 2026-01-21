# Functions
# Author: Audrey
# 10 October



def create_mood_message(name, mood="neutral"):
        # create_mood_message = input("How are you feeling today?")
    if mood == "happy":
        return f"Hey{name}, great to see you smiling!"
    elif mood == "sad":
        return f"I hope your day gets better {name}"
    else:
        return f"Hi {name}, hope you're having a good day!"

result = create_mood_message("audrey, happy")
print(result)


def average(num_one, num_two, num_three):
    num_one = int(num_one)
    num_two = int(num_two)
    num_three = int(num_three)
    average = (num_one + num_two + num_three) / 3
    return average

result = average(90,93,93)
print(result)
