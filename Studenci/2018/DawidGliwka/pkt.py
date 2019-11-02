import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, pkt2):
        return math.sqrt(abs(self.x-pkt2.x)**2+abs(self.y-pkt2.y)**2)

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def area(self):
        return abs(p1.x-p2.x)*abs(p1.y-p2.y)


def distance(p1, p2):
    return math.sqrt(abs(p1.x-p2.x)**2+abs(p1.y-p2.y)**2)

pkt  = Point(0, 0)
pkt2 = Point(2, 2)


print(pkt.x, pkt.y)
print(pkt2.x, pkt2.y)
    
print(distance(pkt, pkt2))
print(pkt.distance(pkt2))
rect = Rectangle(pkt, pkt2)
print(rect.area)
