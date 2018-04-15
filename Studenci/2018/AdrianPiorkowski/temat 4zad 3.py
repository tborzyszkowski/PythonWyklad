class punkt:

    def __init__(self):
        self.x=0
        self.y=0

    def ustaw(self,a,b):
        self.x=a
        self.y=b

class prostokat(punkt):
    def __init__(self):
        punkt.__init__(self)
        self.wysokosc=0
        self.szerokosc=0

    def stworz(self,a,b,c,d):
        self.ustaw(a,b)
        self.wysokosc=c
        self.szerokosc=d

    def pole(self):
        return self.wysokosc*self.szerokosc

    def obwod(self):
        return 2 * self.wysokosc + 2 * self.szerokosc

    def srodek(self):
        x=self.x+self.szerokosc/2
        y=self.y+self.wysokosc/2
        print(x,y)

prostokat=prostokat()
prostokat.stworz(1,1,2,2)

print('pole')
print(prostokat.pole())
print('obwod')
print(prostokat.obwod())
print('srodek')
prostokat.srodek()