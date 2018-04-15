from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def length(x1, y1, x2, y2):
    return sqrt(((x2 - x1)**2) + ((y2-y1)**2))

point_1 = Point(2, 3)
point_2 = Point(2, 4)

print length(point_1.x, point_1.y, point_2.x, point_2.y)
#-------------------------------------------


class Rectengle():
    def __init__(self, height, weight, x, y):
        self.height = height
        self.weight = weight
        self.x = x
        self.y = y

    def area(self):
        return self.height * self.weight

    def circuit(self):
        return self.height*2 + self.weight*2

    def points(self):
        return [(self.x, self.y),(self.x+self.weight, self.y), (self.x, self.y + self.height), (self.x + self.weight, self.y + self.height)]


a = Rectengle(2,3,0,0)
print a.area()
print a.circuit()
print a.points()
