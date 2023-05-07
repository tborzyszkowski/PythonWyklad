from Laboratorium._04_klasy.Ludzie.Czlowiek import *

class Student(Czlowiek):
    def __init__(self, imie="Ala", nazwisko="Kociubinska", indeks=111111) -> None:
        Czlowiek.__init__(self, imie, nazwisko)
        self.indeks = indeks

if __name__ == "__main__":
    st = Student("Janusz")
    print(st.indeks)
    print(st.nazwisko)