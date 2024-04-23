import random

class Point:

    def __init__(self, x, y):
        """
        This will be called when instantiating an object
        :param x: the value of x
        :param y: the value of y
         """
        self.x = x
        self.y = y

    def __str__ (self):
        """
        This will return the string value used in printing the point
        :return:
        """
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """
        this is when the point is in a list or other container
        :return:
        """
        return self.__str__()

    def distance_origin(self):
        """
        calculate the distance to origin of this point
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        define how a point is greater than another
        :param other: the other point to compare against
        """
        return self.distance_origin() > other.distance_origin()

    def __eq__(self, other):
        """
        define when 2 points are equal
        :param other:
        """
        return self.distance_origin() == other.distance_origin()

if __name__ == "__main__":
    a = Point(2,3)
    b = Point(7, 9)

    print(f"a=({a.x},{a.y})")
    print(f"b=({b.x},{b.y})")

    #creating a list of 5 random points
    points = [] # initialize an empty list
    for _ in range(5):
       # x = random.randint(-100,100)
       # y = random.randint(-100,100)
       # random_point = Point(x,y)
       # points.append(random_point)
        # or in a single line like this
        points.append(Point(random.randint(-100,100),
                            random.randint(-100, 100)))

    for point in points:
        print(f"p{point.x},{point.y})")

    # try to print the first point
    print("printing a point value:", points[0])
    print(points)
    a = Point(3,4)
    print(f"distance origin a= {a.distance_origin()}")
    b = Point(5,12)
    print(f"distance origin b= {b.distance_origin()}")
    print(f"a > b = {a>b}, a < b = {a < b}")

    points.sort()
    print(f"largest point in the list is {points[-1]}") # the largest is the last in ordered list
