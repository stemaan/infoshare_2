# @TODO: klasa Person
# @TODO: atrybuty: imie, nazwisko, ulica, nr, miasto, miasto_gmin, kod_pocztowy, adres jako atrybut ukryty
# @TODO: "Wadowicka 6d, 30-415 Krakow"
# @TODO: "Jakaswes 144, 12-345 MiastoGminne"
# @TODO: p.adres -> "Wadowicka 6d, 30-415 Krakow"
# @TODO: p2.adres -> "Jakaswes 144, 12-345 MiastoGminne"
# @TODO: f'{ulica}|{miasto} {nr}, {kod} {miasto}|{miasto2}"
class Person:
    def __init__(self, imie, nazwisko, ulica='', nr='', miasto='', miasto_gmin='', kod=''):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nr = nr
        self.miasto = miasto
        self.miast_gminne = miasto_gmin
        self.kod_pocztowy = kod
        self.__adres = ''

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.ulica} {self.nr} {self.miasto} {self.miast_gminne} {self.kod_pocztowy}'

    @property
    def adres(self):
        if self.ulica:
            return f'{self.ulica} {self.nr}, {self.kod_pocztowy} {self.miast_gminne}'
        else:
            return f'{self.miasto} {self.nr}, {self.kod_pocztowy} {self.miast_gminne}'

if __name__ == '__main__':
    jan = Person(
        'Jan', 'Kowalski', 'Wadowicka', '6d', 'Krakow', 'Krakow', '30-415'
    )
    adam = Person(
        'Adam', 'Nowak', nr='144', miasto='Wies', miasto_gmin='Miasto', kod='12-345'
    )
    print(jan)
    print(adam)
    print(adam.adres)
    print(jan.adres)