import random

class Foo(random.choice([int, float, str, unicode, Exception])):
    pass

f = Foo('1')
print f