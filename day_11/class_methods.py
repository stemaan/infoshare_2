class Pracownik:
    liczba_pracownikow = 0
    roczna_podwyzka = 0.1

    @classmethod
    def utworz_z_pensja(cls, stanowisko, amount):
        p = cls(stanowisko)  # Pracownik(stanowisko)
        p.ustaw_wynagrodzenie(amount)
        return p

    @staticmethod
    def daj_podwyzke(pracownik):
        # roczna_podwyzke*wynagrodzenie + wynagrodzenia
        amount = Pracownik.roczna_podwyzka * pracownik.wynagrodzenie
        amount += pracownik.wynagrodzenie
        pracownik.ustaw_wynagrodzenie(amount)

    @staticmethod
    def wyswietl_liczbe_pracownikow():
        print(Pracownik.liczba_pracownikow)

    def __init__(self, stanowisko):
        self.wynagrodzenie = 0
        self.stanowisko = stanowisko
        Pracownik.liczba_pracownikow += 1

    def ustaw_wynagrodzenie(self, amount):
        self.wynagrodzenie = amount


if __name__ == '__main__':
    p = Pracownik('aktor')
    print(f'Liczba pracownikow {Pracownik.liczba_pracownikow}')
    p2 = Pracownik('dyrektor')
    print(f'Liczba pracownikow {Pracownik.liczba_pracownikow}')
    p.ustaw_wynagrodzenie(2300)
    p2.ustaw_wynagrodzenie(3300)
    print(f'Pracownik p zarabia {p.wynagrodzenie}')
    print(f'Pracownik p2 zarabia {p2.wynagrodzenie}')
    p3 = Pracownik.utworz_z_pensja('kierowca', 4000)
    print(f'Liczba pracownikow {Pracownik.liczba_pracownikow}')
    print(f'Pracownik p3 zarabia {p3.wynagrodzenie}')
    del p2
    print(f'Liczba pracownikow {Pracownik.liczba_pracownikow}')
    Pracownik.daj_podwyzke(p)
    print(f'Pracownik p zarabia {p.wynagrodzenie}')
    Pracownik.wyswietl_liczbe_pracownikow()


