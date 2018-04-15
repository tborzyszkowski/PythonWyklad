class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.area = abs(p1.x-p2.x)*abs(p1.y-p2.y)

pkt  = Point(13, 14)
pkt2 = Point(16, 23)
print(pkt.x, pkt.y)
rect = Rectangle(pkt, pkt2)
print(rect.area)
