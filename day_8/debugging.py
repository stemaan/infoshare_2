import os
# dane
monety =        [0, 2, 1, 0.5, 0.2, 0.1]
monety_reszta = [0, 0, 0,   0,   0,   0]

banknot = 20
zakup = 8.30
reszta = banknot - zakup
# tekst = input('wpisz cos')
# indeks do trzymania pozycji listy
indeks_mon_reszta = 0

for moneta in monety:
    if reszta >= moneta:
        try:
            ilosc = reszta // moneta
            wartosc = ilosc * moneta
            reszta = reszta - wartosc
        except (ZeroDivisionError, NameError) as error:
            continue
        wartosc = ilosc * moneta
        reszta = reszta - wartosc

        monety_reszta[indeks_mon_reszta] = ilosc

    indeks_mon_reszta += 1

print("Reszta do wydania:")

print(monety)
print(monety_reszta)