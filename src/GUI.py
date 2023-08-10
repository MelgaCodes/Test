import PySimpleGUI as sg
import random
import json


label_language = sg.Text("What to what language do you want to translate to?")
button_spanish = sg.Button("Spanish")
button_polish = sg.Button("Polish")

window = sg.Window("Let's translate!",
                   layout= [[label_language],[button_spanish, button_polish]])

event = window.read()

if event[0] == "Spanish":
    language = "Spanish"
elif event[0] == "Polish":
    language = "Polish"

window.Close()

label_category = sg.Text("Choose a category")
button_fruits = sg.Button("Fruits")
button_transport = sg.Button("Transport")
button_clothes = sg.Button("Clothes")

window = sg.Window("Let's translate!",
                   layout= [[label_category],
                            [button_fruits, button_transport, button_clothes]])
event = window.Read()

if event[0] == "Fruits":
    category = "Fruits"
elif event[0] == "Transport":
    category = "Transport"
elif event[0] == "Clothes":
    category = "Clothes"

window.Close()

with open(f"../data/{category}.json") as file:
    data = json.load(file)

preliminary_list = list(data[f"{category}".lower()])
final_list = []

for i in range(0, 10):
    rand_item = random.choice(preliminary_list)
    final_list.append(rand_item)
    preliminary_list.remove(rand_item)

label_to_translate = sg.Text("Words to translate")

label1 = sg.Text(f"{final_list[0]}")
label2 = sg.Text(f"{final_list[1]}")
label3 = sg.Text(f"{final_list[2]}")
label4 = sg.Text(f"{final_list[3]}")
label5 = sg.Text(f"{final_list[4]}")
label6 = sg.Text(f"{final_list[5]}")
label7 = sg.Text(f"{final_list[6]}")
label8 = sg.Text(f"{final_list[7]}")
label9 = sg.Text(f"{final_list[8]}")
label10 = sg.Text(f"{final_list[9]}")

input1 = sg.Input()
input2 = sg.Input()
input3 = sg.Input()
input4 = sg.Input()
input5 = sg.Input()
input6 = sg.Input()
input7 = sg.Input()
input8 = sg.Input()
input9 = sg.Input()
input10 = sg.Input()

button_submit = sg.Button("Submit")

window = sg.Window("Let's translate!",
                   layout = [[label1, input1],
                             [label2, input2],
                             [label3, input3],
                             [label4, input4],
                             [label5, input5],
                             [label6, input6],
                             [label7, input7],
                             [label8, input8],
                             [label9, input9],
                             [label10, input10],
                             [button_submit]
                             ])

window.Read()
