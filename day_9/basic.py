class Samochod:
    def __init__(self, marka, model, start=False):
        print('wywoluje __init__')
        self.marka = marka
        self.model = model
        self.uruchomiony = start

    def __str__(self):
        return f'Samochod marki {self.marka} model {self.model} uruchomiony? {self.uruchomiony}'

    def __len__(self):
        return len(self.marka)

    def uruchom_samochod(self):
        self.uruchomiony = True

    def wylacz_samochod(self):
        self.uruchomiony = False


if __name__ == '__main__':
    print('przed utworzeniem instancji')

    golf = Samochod('Volkswagen', 'Golf')
    print('po utworzeniu instancji')
    print(golf)
    golf.uruchom_samochod()
    print(golf)

    megane = Samochod('Renault', 'Megane', start=True)
    print(megane)
    megane.wylacz_samochod()
    print(megane)
    print(len(megane))
