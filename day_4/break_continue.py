counter = 0
value = input('Podaj liczbe: ')
value = int(value)

# @TODO: wyswietl na ekran wartosc counter
# @TODO: wyswietl tylko jesli counter jest nieparzysty
while counter < value:
    # ten kod wykonuje sie w petli
    if counter % 2:
        print(counter)
        counter += 1
    elif value > 1000:
        break
    else:
        counter += 1
        continue
# ten juz poza petla
print('bye')
