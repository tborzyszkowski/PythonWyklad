
class Czlowiek:
    def __init__(self, imie, nazwisko) -> None:
        self.imie = imie
        self.nazwisko = nazwisko

    @property
    def imie(self):
        return self.__imie

    @imie.setter
    def imie(self, imie):
        self.__imie = "NoneJan" if imie is None else imie

    @property
    def nazwisko(self):
        return self.__nazwisko

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        if self.nazwisko_is_valid(nazwisko):
           self.__nazwisko = nazwisko
        else:
            raise Exception()

    def nazwisko_is_valid(self, nazwisko):
        return nazwisko is not None