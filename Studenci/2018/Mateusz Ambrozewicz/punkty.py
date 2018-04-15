import math

class Punkt:
    """Klasa punkt"""
    def __init__(self,odcieta,rzedna):
        self.x = odcieta
        self.y = rzedna


def oblicz_odl(P1,P2):
    dx = abs(P1.x-P2.x)
    dy = abs(P1.y-P2.y)
    wynik = math.sqrt(pow(dx,2)+pow(dy,2))
    return wynik

print oblicz_odl(Punkt(1,1),Punkt(5,5))
