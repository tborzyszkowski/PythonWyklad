import random
from abc import ABC, abstractmethod

class Kolor(ABC):
    @abstractmethod
    def jest_czerwony(self):
        pass

    @abstractmethod
    def jest_zielony(self):
        pass

class Ksztalt:
    def __init__(self, nazwa = "kształt"):
        self.nazwa = nazwa

    def rysuj(self):
        return self.nazwa

class Kolo(Ksztalt, Kolor):
    def __init__(self, nazwa = "kolo", promien = 5):
        Ksztalt.__init__(self, nazwa)
        self.promien = promien

    def rysuj(self):
        return Ksztalt.rysuj(self) + \
            ", promień: " + \
            str(self.promien) + \
            ", zielony: " + str(self.jest_zielony())+ \
            ", czerwony: " + str(self.jest_czerwony())

    def jest_czerwony(self):
        return True if self.promien % 2 == 0 else False

    def jest_zielony(self):
        return False


class Kwadrat(Ksztalt, Kolor):
    def __init__(self, nazwa = "kwadrat", bok = 4):
        Ksztalt.__init__(self, nazwa)
        self.bok = bok

    def rysuj(self):
        return Ksztalt.rysuj(self) + \
            ", bok: " + str(self.bok) + \
            ", zielony: " + str(self.jest_zielony())+ \
            ", czerwony: " + str(self.jest_czerwony())

    def jest_czerwony(self):
        return False

    def jest_zielony(self):
        return True


if __name__ == "__main__":
    ksztalt = Ksztalt("ksztalt_1")
    kolo = Kolo("kolo_2")
    kwadrat = Kwadrat("kwadrat_3")

    # print(ksztalt.rysuj())
    # print(kolo.rysuj())
    # print(kwadrat.rysuj())

    # ksztalt = kolo
    # print(ksztalt.rysuj())
    # ksztalt = kwadrat
    # print(ksztalt.rysuj())

    wybor = random.choice([True, False])
    if wybor:
        ksztalt = kolo
    else:
        ksztalt = kwadrat
    print(ksztalt.rysuj())
