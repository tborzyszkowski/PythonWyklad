class Sum:
    def __add__(self, x):
        self.pole = 1;
        print "Brak implementacji"
    def __str__(self):
        return str(self.pole)

class ListSum(Sum):
    def __init__(self, l=[]):
        self.pole = l
    def __add__(self, x):
        self.pole += x.pole
        return self
    
class DicSum(Sum):
    def __init__(self, l={}):
        self.pole = l
    def __add__(self, x):
        self.pole.update(x.pole)
        return self

a = ListSum([1,2,3])
b = ListSum(['a', 'b', 'c'])

print a

print a + b

x = DicSum({1:'a'})
y = DicSum({2:'b'})

print x + y