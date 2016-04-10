from abc import ABCMeta, abstractmethod


class Literkowanie:
    __metaclass__ = ABCMeta

    @abstractmethod
    def getLiterka(self):
        pass

    # def printWzor(self, n=5):
    #     lit = self.getLiterka()
    #     if lit:
    #         return (""+lit) * n
    #     else:
    #         return None
    def printWzor(self, n=5):
        return (""+self.getLiterka()) * n


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
# l = Literkowanie()
# print l.printWzor()


class LiterkowanieWrong(Literkowanie):
    def getString(self):
        return "Ala ma kota"

l = LiterkowanieWrong()
print l.getString()
