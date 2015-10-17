import pickle

class Maz:
    def __init__(self,n, z=None):
        self.name = n
        self.zona = z
    def setZona(self, z):
        self.zona = z
    def __repr__(self):
        if self.zona:
            return "Maz: %s : Zona: %s" % (self.name, self.zona.name)
        else:
            return "Maz: %s : Zona: %s" % (self.name, "None")
class Zona:
    def __init__(self,n,m=None):
        self.name = n
        self.maz = m
    def setMaz(self, m):
        self.maz = m
    def __repr__(self):
        if self.maz:
            return "Zona: %s : Maz: %s" % (self.name, self.maz.name)
        else:
            return "Zona: %s : Maz: %s" % (self.name, "None")

m = Maz("Zenek")
print m
z = Zona("Barbara")
print z

m.setZona(z)
z.setMaz(m)

print m, z

print '-------------'
sm = pickle.dumps(m)
mm = pickle.loads(sm)

print sm
print mm