from Secondary import game


lang = ""

while lang != "spanish" and lang != "polish":
    lang = input("To what language do you want to translate? ")

results = game(lang)
score = results[0]
perfect_score = results[1]

if perfect_score:
    print(f"Your final score is {score}. Congrats, you are an ace!")
else:
    print(f"Your final score is {score}")