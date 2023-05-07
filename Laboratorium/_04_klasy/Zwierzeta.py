class Zwierz:
    def replay(self):
        return self.glos()

    def glos(self):
        pass


class Ssak(Zwierz):
    def glos(self):
        return "Ssak: glos"


class Kot(Ssak):
    def glos(self):
        return "Kot: glos"


class Pies(Ssak):
    def glos(self):
        return "Pies: glos"


class Naczelny(Ssak):
    def glos(self):
        return "Naczelny: glos"


class Haker(Naczelny):
    pass
    # def glos(self):
    #     return "Naczelny: glos"

p = Pies()
k = Kot()

print p.replay() + k.replay()

h= Haker()
print h.replay()