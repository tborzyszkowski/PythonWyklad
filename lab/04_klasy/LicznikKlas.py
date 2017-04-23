class A:
    licznik = 0
    def __init__(self):
        self.nr = self.__class__.licznik
        self.__class__.licznik += 1

    def numberOfObjects(self):
        return self.__class__.licznik

x1 = A()
x2 = A()
x3 = A()

print x1.numberOfObjects()
print x2.numberOfObjects()
print x3.numberOfObjects()

print x1.nr
print x2.nr
print x3.nr
