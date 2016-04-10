from abc import *


class Literkowanie:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getLiterka(self):
        pass

    def printWzor(self, n=5):
        lit = self.getLiterka()
        if lit:
            return (""+lit) * n
        else:
            return None


class LiterkowanieA(Literkowanie):
    def getLiterka(self):
        return "A"


class LiterkowanieB(Literkowanie):
    def getLiterka(self):
        return "B"


lA = LiterkowanieA()
print lA.printWzor(n=10)
lB = LiterkowanieB()
print lB.printWzor()
l = Literkowanie()
print l.printWzor()
