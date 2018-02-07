data = input('Podaj liczbe lub litere: ')

while not data.isalpha() and not data.isdigit():
    print('Podales zle dane, podaj jeszcze raz')
    data = input('Podaj liczbe lub litere: ')

if data.isdigit():
    print('Podales liczbe')
elif data.isalpha():
    print('Podales litere')
print('bye!')