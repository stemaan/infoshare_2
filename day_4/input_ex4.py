#@ TODO: uzytkownik podaje dane i oczekujemy ze dane to liczba oraz
#@ TODO: ze jesli jest to liczba to też jest różna od zera
data = input('Podaj liczbe roza od zera: ')

while not data.isdigit() or int(data) == 0:
    print('Podales zle dane, podaj jeszcze raz')
    data = input('Podaj liczbe rozna od zera: ')

print('bye')
