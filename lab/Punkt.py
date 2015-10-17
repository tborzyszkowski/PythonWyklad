import math

class Wektor:
    def __init__(self, x=0, y=0 ):
        self.a=x
        self.b=y
        
class Punkt:
    def __init__(self, x=0, y=0 ):
        self.a=x
        self.b=y
    def odleglosc(self, p):
        return math.sqrt((p.a-self.a)**2+(p.b-self.b)**2)
    def przesun(self, w):
        return Punkt(self.a+w.a, self.b+w.b)
    def __str__(self):
        return "("+str(self.a)+", "+str(self.b)+")"

p = Punkt()
#print p
#print p.przesun(Wektor(1,1))
print p.odleglosc(p.przesun(Wektor(1,1)))

class Prostokat:
    def __init__(self, x=0, y=0, dx=1, dy=1 ):
        self.p = Punkt(x,y)
        self.dx=dx
        self.dy=dy
    def pole(self):
        return self.dx*self.dy
    def obwod(self):
        return 2*(self.dx+self.dy)
    def przesun(self, w):
        return Prostokat(self.p.a+w.a, self.p.b+w.b,self.dx, self.dy)
    
print Prostokat().pole()
print Prostokat().obwod()
print Prostokat().przesun(Wektor(1,1)).obwod()
