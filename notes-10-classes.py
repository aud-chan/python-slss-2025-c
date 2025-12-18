# Classes and Objects
# Author: Audrey
# 11 December 2025


import random
from tkinter import YES

class Pokemon:
    def __init__(self):
        """Contructor"""
        self.name = ""
        self.species = ""
        self.type = "normal"
        self.level = 1
        self.age = 0
        self.move = "Spin"
        # 1 in 4096
        if random.randint(0,4096):
            self._is_shiny = False
        else:
            self._is_shiny = True
            print("This Pokemon is shiny")
        print("A pokemon is born!")

    def talk(self):
        """Hear what the pokemon has to say. The pokemon says its species name"""
        print(f"{self.name} says \"{self.species}\".")

    def stats(self):
        """Display the stats of the pokemon"""
        print(f"------{self.species}---------")
        print(f"      Name: {self.name}")
        print(f"      Type: {self.type}")
        print(f"      Age: {self.age}")
        print(f"      Level: {self.level}")
        print("---------------------------")

    def dance(self):
        """Make the pokemon dance"""
        print(f"{self.name} is doing a {self.move}")

class Squirtle(Pokemon):
    def __init__(self):
        # Call the constructor of Pokemon
        super().__init__()
        self.name = "Squirtle"
        self.species = "Squirtle"
        self.type = "water"

    def water_gun(self):
        """Squirtle shoots water out of its mouth"""
        print(f"{self.name} used water gun!")


class Pikachu(Pokemon):
    def __init__(self):
        # Call the constructor of Pokemon
        super().__init__()
        self.name = "Pikachu"
        self.species = "Pikachu"
        self.type = "electric"

    def thunder_bolt(self):
        """Pikachu throws out a thunderbolt"""
        thunder_bolt = input("Do you want Pikachu to throw a thunderbolt?")
        if thunder_bolt == "yes":
            print(f"{self.name} threw a thunderbolt!")
        else:
            print("Waiting for next move")


    def quick_attack(self):
        """Pikachu attacks you"""
        quick_attack = input("Do you want Pikachu to do a quick attack?")
        if  quick_attack == "yes":
            print(f"{self.name} threw an attack!")
        else:
            print("Waiting for next move")





if __name__ == "__main__":
    # create a pokemon object
    pokemon_one = Pokemon()
    # access the pokemon's properties
    print("Pokemon name: ", pokemon_one.name)
    # change the  pokemon's properties
    pokemon_one.name = "Gary"
    pokemon_one.species = "Pikachu"
    print("Pokemon name: ", pokemon_one.name)
    # create another pokemon object
    pokemon_two = Pokemon()
    pokemon_two.name = "Pikachu"
    pokemon_two.species = "Pikachu"
    # check to see if a value is a pokemon
    if pokemon_one == pokemon_two:
        print("They're the same")
    else:
        print("They're individual pokemon")

    if type(pokemon_one) is Pokemon:
       print(f"{pokemon_one.name} is a Pokemon")

    # tell our pokemon to talk
    pokemon_one.talk()
    pokemon_two.talk()

    pokemon_one.stats()
    pokemon_two.stats()

    pokemon_one.dance()
    pokemon_two.dance()

    squirtle_one = Squirtle()
    # use .water_gun()
    squirtle_one.water_gun()
    # use .talk()
    squirtle_one.talk()

    pikachu_one = Pikachu()
    pikachu_one.thunder_bolt()
    pikachu_one.quick_attack()
