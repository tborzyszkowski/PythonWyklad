import random


class Foo(random.choice([int, float, str, Exception])):
    pass


f = Foo('1')
print(f)
