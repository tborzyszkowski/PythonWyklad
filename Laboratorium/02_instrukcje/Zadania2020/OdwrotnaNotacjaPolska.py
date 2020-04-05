
def wylicz(wyrazenie):
    """
    Dla zadanego w postaci napisu wyrazenia w ONP wylicza jego wartosc.

    :param wyrazenie: naspis reprezentujacy wyrazenie w ONP; poszczegolne czlony wyrazenia rozdzielone spacja
    :return: wynik
    """
    operacje = {
        "+": (lambda x, y: x + y),
        "-": (lambda x, y: x - y),
        "*": (lambda x, y: x * y)
    }

    lista_tokenow = wyrazenie.split()
    stos = []
    for element in lista_tokenow:
        if element.isdigit():
            stos.append(int(element))
        elif element in operacje.keys():
            if len(stos) < 2:
                raise ValueError("Brak argumentow dla opracji %s" % element)
            stos.append(operacje[element](stos.pop(), stos.pop()))
        else:
            raise ValueError("To wyrazenie jest jakies dziwne: %s" % element)
    return stos

if __name__ == "__main__":
    print wylicz("1 2 + 3 *")