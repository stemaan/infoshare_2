people = {
    'kowalski': 'jan',
    'nowak': 'adam'
}

lastname = input('Podaj nazwisko: ')

# bad
if lastname in people:
    print(people[lastname])

# better
message = 'Nazwisko nie istnieje w bazie!'
print(people.get(lastname, message))

# the best
try:
    print(people[lastname])
except KeyError as keyerr:
    print(f'Nie ma takiego nazwiska jak: {keyerr}')

filename = input('Podaj nazwe pliku: ')

try:
    plik = open(filename)
    print(plik.read())
except FileNotFoundError as error:
    print(f'Pliku nie znaleziono: {error.filename}')
finally:
    print('goodbay')
