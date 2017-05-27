#35

from math import sqrt

class Point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_info(self):
        print("Point: x = %d , y = %d" % (self.x, self.y))

class Circle():

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def print_info(self):
        print("Circle: x = %d , y = %d, radius = %d" % (self.x, self.y, self.r))


    def point_in_circle(self, point):

        point_circle = sqrt(pow(self.x - point.x, 2) + pow(self.y - point.y, 2))
        if point_circle <= self.r:
            return True
        else:
            return False

if __name__ == "__main__":

    circle = Circle(2, 4, 5)
    point = Point(6, 5)

    circle.print_info()
    point.print_info()

    if circle.point_in_circle(point) == True:
        print()
        print ("Point in the circle")
    else :
        print()
        print("Point not in the circle")

