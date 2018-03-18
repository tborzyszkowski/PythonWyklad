class Animal:
    legs = 4

    def __init__(self, color, name):
        self.color = color
        self.name = name


class Pies(Animal):
    def bark(self):
        print("Woof!")


class Kot(Animal):
    def purr(self):
        print("Purr!")


fido = Pies("black", "Fido")

print "Dogs name is", fido.name
print "He's", fido.color
fido.bark()
