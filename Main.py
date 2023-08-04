from Secondary import game

list_fruits = ['apple', 'banana', 'peach', 'pear', 'strawberry', 'melon', 'watermelon']
list_fruits_translated = ['manzana', 'platano', 'melocoton', 'pera', 'fresa', 'melon', 'sandia']

list_transport = ['car', 'bike', 'motorbike', 'bus', 'train', 'truck', 'plane', 'ship']
list_transport_translated = ['coche', 'bicicleta', 'moto', 'autobus', 'tren', 'camion', 'avion', 'barco']

game_category = ''

while game_category != 'fruits' and game_category != 'transport':
    game_category = input("Choose a category: fruits or transport.\n")

if game_category == 'fruits':
    game(list_fruits, list_fruits_translated)

elif game_category == 'transport':
    game(list_transport, list_transport_translated)
