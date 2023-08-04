from random import randint
import json

def game(lang):

    score = 0
    perfect_score = False

    with open("data.json") as file:
        data = json.load(file)

    fruit = list(data["fruit"])

    for item in fruit:
        local_dict = data["fruit"][item]
        user_choice = input("What is the translation of " + item + "\n")
        if user_choice == local_dict["translation"][lang]:
            print("That is correct!\n")
            score += 1

        else:
            print("That is not correct\n")

    if score == len(fruit):
        perfect_score = True

    return [score, perfect_score]