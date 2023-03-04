class Point:
    def __init__(self, x_coordinate = 0, y_coordinate = 0) -> None:
        self.x = x_coordinate
        self.y = y_coordinate

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.is_valid(x):
           self.__x = x
        else:
            raise Exception()

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y if y >= 0 else -y

    def distance(self, point):
        return 0

    def is_valid(self, val):
        return val >=0;

if __name__ == "__main__":
    try:
        p = Point(-3, -4)
        print(p.x, p.y)
    except:
        print("Nie udało się")
    # p.x = -10
    # print(p.x, p.y)
