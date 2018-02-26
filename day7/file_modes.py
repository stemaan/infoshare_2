# constant value
FILENAME = 'dlugosc_pliku.txt'

print('tryb to odczytu')
with open(FILENAME, 'r') as plik:
    cursor = plik.tell()
    print('przed odczytem', cursor)
    print(plik.read())
    print('po odczycie')
    cursor = plik.tell()
    print(cursor)

print('tryb do zapisu')
with open(FILENAME, 'w') as plik:
    print(plik.read())

print('tryb dopisywania')
with open(FILENAME, 'r+') as plik:
    cursor = plik.tell()
    print('pozycja kursora w trybie rw', cursor)
    plik.seek(0)
    cursor = plik.tell()
    print('kursor przestawiony na pozycje: ', cursor)
    plik.write('ala ma kota, kot ma ale\n')


