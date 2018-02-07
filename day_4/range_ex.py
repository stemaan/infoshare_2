value = int(input('Podaj liczbe:'))
# value = int(value)

# @TODO: wyswietl kolejne liczby parzyste bez instrukcji warunkowych
start = 0
stop = value
step = 2
for idx in range(start, stop, step):
    print(idx)