from Laboratorium._04_klasy.Ludzie.Czlowiek import *

def test_empty_nazwisko_is_not_valid():
    nazwisko = None
    valid = Czlowiek.nazwisko_is_valid(nazwisko)
    assert not valid

def test_nazwisko_is_valid():
    nazwisko = "Kowalski"
    valid = Czlowiek.nazwisko_is_valid(nazwisko)
    assert valid
