import random


class Foo(random.choice([int, float, str, Exception])):
    pass

if __name__ == '__main__':
    f = Foo('1')
    print(f, isinstance(f, int), isinstance(f, float), isinstance(f, str), isinstance(f, Exception))
