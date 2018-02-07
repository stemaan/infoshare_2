#@ TODO: pobierz od uzytkownika dwolona liczbe lub znak
#@ TODO: sprawdz czy wprowadzone dane to liczba lub litera
#@ TODO: wyswietl stosowny komunikat dla np. 'wprwadziles dane typu: liczba'
data = input('Podaj liczbe lub litere: ')

if data.isdigit():
    print('Podales liczbe')
    print('bye!')
elif data.isalpha():
    print('Podales litere')
    print('bye!')
else:
    print('HELP!')
