phonebook = {
    'Kowalski': 123,
    'Nowak': 456,
    'Iksinski': 789
}

# lastname = input('Podaj nazwisko: ')

# pobranie wartosci z klucza Kowalski
# print(phonebook[lastname])


lastname = 'XYZ'
print(phonebook.get(lastname, 'Brak takiego nazwiska!'))

# print(phonebook[lastname])

new_phonebook = phonebook.copy()
print(new_phonebook)
new_members = {'XYZ': 1, 'ABC': 2}
# scalenie slownikow
new_phonebook.update(new_members)
print(new_phonebook)

new_phonebook['XYZ'] = 0
print(new_phonebook)
# update nadpisze dane
new_phonebook.update({'XYZ': 5})
print(new_phonebook)
new_phonebook.update(Kowalski=898, Nowak=111)
print(new_phonebook)

