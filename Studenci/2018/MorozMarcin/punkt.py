import math

class Punkt:
    def __init__(self, wsp1, wsp2):
        self.wsp1 = wsp1
        self.wsp2 = wsp2


class Odcinek:
    def __init__(self, punkt1, punkt2):
        self.punkt1 = punkt1
        self.punkt2 = punkt2

    def Odleglosc(self):
        return math.sqrt(pow(self.punkt1.wsp1-self.punkt2.wsp1, 2) + pow(self.punkt1.wsp2-self.punkt2.wsp2, 2))


class Prostokat:
    def __init__(self, punkt, szerokosc, wysokosc):
        self.punkt = punkt
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc


    def Pole(self):
        return abs(self.szerokosc * self.wysokosc)

    def Obwod(self):
        return 2*self.szerokosc + 2* self.wysokosc

    def Srodek(self):
        return Punkt(self.punkt.wsp1 + self.szerokosc/2, self.punkt.wsp2 + self.wysokosc/2)



p1 = Punkt(2,2)
p2 = Punkt(5,6)

o1 = Odcinek(p1, p2)

print "Odleglosc = " + str(o1.Odleglosc())

pr = Prostokat(p1, 4 , 2)

print "Pole = " + str(pr.Pole())

print "Obwod = " + str(pr.Obwod())

print "Srodek = [" + str(pr.Srodek().wsp1) + "," + str(pr.Srodek().wsp2) + "]"
