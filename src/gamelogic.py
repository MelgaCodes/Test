import json
import random


def game(lang, topic):

    score = 0
    perfect_score = False

    with open(f"../data/{topic}.json") as file:
        data = json.load(file)

    the_list = list(data[f"{topic}"])

    for i in range(0, 10):
        rand_item = random.choice(the_list)
        local_dict = data[f"{topic}"][rand_item]
        user_choice = input("What is the translation of " + rand_item + "\n")
        the_list.remove(rand_item)

        if user_choice == local_dict["translation"][lang]:
            print("That is correct!")
            score += 1

        else:
            print("That is not correct")

    if score == 10:
        perfect_score = True

    return [score, perfect_score]
