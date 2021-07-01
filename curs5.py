# memory savers, files and web scraping
# lambda, map, filter, zip, list comprehension
# lucrul cu fisiere
# pip si virtual environment
# web scraping

#lambda - functie anonima, un sigur task, orice numar de parametri(tot doar o instructiune)
my_lambda = lambda x, y: x+y     # do not assign it, use def
my_sum = my_lambda(2, 3)
print(my_sum)

import copy

players = [
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'rank': 3
    },
    {
        'first_name': 'Ron',
        'last_name': 'McDonald',
        'rank': 1
    },
    {
        'first_name': 'Brad',
        'last_name': 'Kelvin',
        'rank': 2
    }
]

sorted_players = sorted(players, key=lambda player: player['rank'])
print(sorted_players)

# functia map


def check_top_3_player(player):
    updated_player = copy.deepcopy(player)
    # altfel se facea prin referinta si nu vrem asta; dict(player) - merge daca nu e dictionar in dictionar
    updated_player['is_top_3'] = True if player['rank'] <= 3 else False
    # player['rank'] <= 3
    return updated_player


top_players = list(map(check_top_3_player, players))
print(top_players)     # returneaza un obiect de tipul map care este iterabil


# functia filter
all_mcdonalds = list(filter(lambda player: player['last_name'] == 'McDonald', players))
print(all_mcdonalds)


# functia zip - mai multe structuri iterabile, returneaza iterabil zip, cu elemente grupate din structurile initiale

letters = ['a', 'b', 'c', 'z']
numbers = [1, 2, 3]
print(zip(letters, numbers))
for l, n in zip(letters, numbers):
    print(n, l)


# list comprehension
my_numbers = [1, 2, 3, 4, 5]
squared_numbers = [item ** 2 for item in my_numbers]
print(f'Numerele mele sunt {my_numbers}')
print(f'Numerele la patrat sunt {squared_numbers}')

even_squared_numbers = [item ** 2 for item in my_numbers if item % 2 == 0]
print(f'{even_squared_numbers}')
odd_squared_numbers = [item **2 for item in my_numbers if item % 2 != 0]
print(f'{odd_squared_numbers}')


# lucru cu fisiere
print("--" * 20)
# pentru deschidere folosim with - rol de a simplifica gestiunea
#with open('hello.txt', 'w') as file:
#    file.write('hello world')


# r - read, w - write, a - append, r+ - citire si scriere


# fisiere csv (comma separated values)
import csv
with open('cars.csv', 'r') as csv_file:
    rows = csv.reader(csv_file, delimiter = ',')
    for row in rows:
        print(row)