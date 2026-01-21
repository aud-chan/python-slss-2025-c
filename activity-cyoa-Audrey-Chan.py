# Choose your own adventure
# Audrey Chan
# 24 September 2025

# Choose your own adventure story focusing on
# usinf variables and branching/conditionals

# Introduction
import time
import sys

user_name1 = input("What's your name?")

continue_game = input("Start adventure?")
if continue_game == "yes":
    print(f"All right, {user_name1} Let's begin!")
else:
    print("Try again.")
sys.exit

print("You find yourself in the middle of a forest with a map and a note card")
time.sleep(3)
print("On the card it says - Follow the map and get to the little house on the other side. You have 1 hour.")
time.sleep(3)
print("You have no idea how you got here or how to get out.")
time.sleep(3)
print("You head straight to see your first decision. Go up the mountain or through the forest.")
time.sleep(3)


mountain_forest = input("Which way are you going? Mountain or Forest?")
if mountain_forest == "mountain":
    print("You head towards the mountain and start walking up a hill.")
    time.sleep(2)
    print("Big boulders block your way so you have to maneuver through the gaps like a maze.")
    time.sleep(2)
    print("You sit down for a break because it's a steep hill.")
    time.sleep(2)
    print("On the way up you see a magnet hidden behind a rock")
    time.sleep(2)
    magnet = input("Do you pick it up?")
    if magnet == "yes":
        print("Yay! It's now stored in your backpack")
    else:
        print("Ok, continuing on with the story.")
        time.sleep(2)
    print("Finally you reach the top of the mountain and see it's just as long to get down. You have 15 minutes left. But there's a jetpack on the floor")

    time.sleep(2)
    fly_or_walk = input("What do you do? Do you take the jetpack or do you walk down safely?")
    if fly_or_walk == "jetpack":
        print("You turn on the jetpack and fly down the mountain.")
        print("When you land, a crossroad in front of you leads left or right.")
        time.sleep(2)
    left_or_right = input("left or right?")
    if left_or_right == "left":
        print("You continue walking, and see a river. You see metal block on the edge and attempt to push it in.")
        if magnet == "yes":
            print("You use the magnet in your bag to help drag it over the water.")
            time.sleep(2)
            print("You walk over the block and see the house.")
            time.sleep(2)
            print("You made it!")
            sys.exit
    elif left_or_right == "right":
        print("You were teleported to the finish line. You passed!")
        sys.exit

    elif fly_or_walk == "walk":
        print( "You take the safer option and run down at full speed but glance at the map")
        time.sleep(2)
        print("There's still one stop left before you reach the house.")
        time.sleep(2)
        print("You've got to hurry")
        time.sleep(2)
        print("A crossroad in front of you leads left or right.")
        time.sleep(2)
        left_or_right2 = input("left or right?")
        if left_or_right2 == "left":
            print("You see the house but time is up.")
        # sys.exit
        # elif left_or_right2 == "right":
        # print("You were teleported to the finish line. You passed!")
        #     sys.exit

elif mountain_forest == "forest":
    print("You head towards the forest and brush past the trees.")
    print("Walking through you hear sounds in the bushes but choose to ignore it.")
    time.sleep(2)
    print("As you keep walking, the sounds get louder and louder until...")
    time.sleep(2.5)
    print("A big bad wolf jumps out in front of you and says")
    time.sleep(2)
    print('"Hello there! Where are you headed to?"')
    time.sleep(2)
    print("You show the wolf the map in your hands")
    time.sleep(2)
    print("That looks like something I can do! Can I come with you?")
    time.sleep(2)

    yes_nowolf = input("Can the wolf come with you?")
    if yes_nowolf == "yes":
        print("Hurray! The wolf is happy.")
    elif yes_nowolf == "no":
        print("You've made the wolf mad. He opens his big mouth and eats you up.")
        time.sleep(2)
        sys.exit

    if yes_nowolf == "yes":
        print("You continue your journey with the wolf and approach a river.")
        print("You see a log and help push it over the water.")
        print("It wobbles and shakes but you make it over to the other side safely.")
        print("Yay! You see the house and have reached the end goal.")
