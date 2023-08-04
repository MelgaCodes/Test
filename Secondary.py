from random import randint


def game(the_list, the_translated_list):

    score = 0
    control_1 = 1
    while control_1 == 1:
        number_of_words = input("How many words do you want for your test?\n")
        if number_of_words.isnumeric():
            number_of_words = int(number_of_words)
            popper = number_of_words
            control_1 = 0

    for _ in range(0, number_of_words):
        rand_num = randint(0, popper-1)
        answer = input(f"What is the translation of {the_list[rand_num]}\n")
        if answer.lower() == the_translated_list[rand_num]:
            print("That is correct!\n")
            score += 1
            the_list.pop(rand_num)
            the_translated_list.pop(rand_num)
            popper -= 1

        else:
            print("Not correct :(\n")
            the_list.pop(rand_num)
            the_translated_list.pop(rand_num)
            popper -= 1

    print(f"Your final score is {score}")
    return
