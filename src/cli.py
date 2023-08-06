from gamelogic import game


lang = ""
topic = ""

while lang != "spanish" and lang != "polish":
    lang = input("To what language do you want to translate?\n")

while topic != "fruit" and topic != "transport":
    topic = input("What category do you want to play: fruit or transport?\n")

results = game(lang, topic)
score = results[0]
perfect_score = results[1]

if perfect_score:
    print(f"Your final score is {score}. Congrats, you are an ace!")
else:
    print(f"Your final score is {score}")
