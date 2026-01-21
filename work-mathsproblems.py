# Boilerplate
#
#

# Age in 2049 Program
from tkinter.constants import YES
from tokenize import NUMBER


def age():
    questions = [
        "How old are you now?"
    ]
    total = 0
    for question in questions:
        print(question)
    age = int(input("Your age now: "))
    total = 24 + age
    print(f"You age in 2049 will be {total}")

# Olympic judge score average
def judge_scores():
    scores = [
        "Judge 1: ",
        "Judge 2: ",
        "Judge 3: ",
        "Judge 4: ",
        "Judge 5: "
    ]
    total = 0
    for score in scores:
        print(score)

    number = float(input("Score given:  ").strip("?!., "))
    total += number
    average = total / 5
    print(f"Your Olympic Score is {average}".strip("?!., "))



# McDonald's Program
def burger():
    burger = input("Would you like a burger for $5 (Yes/No)").lower().strip("?!., ")
    fries = input("Would you like fries for $3 ").lower().strip("?!., ")

    if burger == "yes":
        plus_tax = 5*1.14
        print(f"Your total is {plus_tax}")
    if fries == "yes":
        plus_tax2 = 3*1.14
        print(f"Your total is {plus_tax2}")
    if burger and fries == "yes":
        total = print(f"Your total is:{plus_tax + plus_tax2}")
        print(total)












def main():
    burger()

if __name__ == "__main__":
    main()
