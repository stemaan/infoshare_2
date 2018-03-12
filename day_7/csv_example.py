# # with open('osoby') as plik:
# #     header = plik.readline()
# #     header = header.strip()
# #     name, lastname, age = header.split(',')
# #     print(f'{name} | {lastname} | {age}')
# #     print('**************')
# #     for line in plik:
# #         print(line.strip())
#
FORMAT = '{name},{lastname},{age}\n'
#
# name = input('Podaj imie')
# lastname = input('Podaj nazwisko')
# age = input('Podaj wiek')
#
# data = ['Jan', 'Kowalski', 33]
#
# with open('osoby', 'a') as plik:
#     plik.writelines(data)

import csv

# with open('osoby') as plik:
#     reader = csv.reader(plik)
#     for line in reader:
#         print(line)

data = ['Jan', 'Kowalski', 33]

with open('osoby', 'a') as plik:
    writer = csv.writer(plik)
    writer.writerow(data)