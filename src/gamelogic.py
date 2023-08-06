import json


def game(lang, topic):

    score = 0
    perfect_score = False

    with open(f"../data/{topic}.json") as file:
        data = json.load(file)

    the_list = list(data[f"{topic}"])

    for item in the_list:
        local_dict = data[f"{topic}"][item]
        user_choice = input("What is the translation of " + item + "\n")
        if user_choice == local_dict["translation"][lang]:
            print("That is correct!\n")
            score += 1

        else:
            print("That is not correct\n")

    if score == len(the_list):
        perfect_score = True

    return [score, perfect_score]
