

class Zwierze:
    def __init__(self, l_konczyn, typ, pozywienie, rozmnazanie, wiek):
        self.wiek = wiek
        self.liczba_konczyn = l_konczyn
        self.typ_poruszania = typ
        self.typ_pozywienia = pozywienie
        self.typ_rozmnazania = rozmnazanie
        self.__foo = 0
        self.hello()

    def hello(self):
        print('zwierze')

    def bar(self):
        self.__foo = 3


class Czlowiek(Zwierze):
    def __init__(self, rasa, wiek, *, l_konczyn=4, typ='chodzacy', pozywienie='wszystko'):
        self.__typ_rozmnazania = 'zyworodny'
        super().__init__(l_konczyn, typ, pozywienie, self.__typ_rozmnazania, wiek)
        self.rasa = rasa

    def hello(self):
        return 'czlowiek'

    def goodbay(self):
        self.__typ_rozmnazania = 'something'


class Student(Czlowiek):
    def __init__(self, rok, kierunek, wiek, imprezowicz, rasa='biala'):
        super().__init__(rasa, wiek)
        self.rok = rok
        self.kierunek = kierunek
        self.imprezowicz = imprezowicz

    def hello(self):
        return 'student'


if __name__ == '__main__':
    student = Student(3, 'IT', 22, False)
    czlowiek = Czlowiek('biala', 23, l_konczyn=5)
    zwierze = Zwierze(2, 'latajacy', 'rosliny', 'niezyworodne', 1)
    # print(isinstance(student, Zwierze))
    # print(isinstance(zwierze, Student))
    # print(issubclass(Student, Zwierze))
    # print(zwierze.hello())
    # print(czlowiek.hello())
    # print(student.hello())
    # print(zwierze)
    print(dir(student))