import random
from point import Point

colors = ["red", "blue", "green", "yellow", "purple", "pink", "beige","bordeaux","marsala", "peach","turqouise", "saffron", "magenta"]

class ColoredPoint(Point): # this class inherits from point
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"{self.color} ({self.x}, {self.y})"

#lets create a list of random 5 colored points
colored_points = []
for _ in range(5):
    colored_points.append(
        ColoredPoint(random.randint(-100,100),
                     random.randint(-100,100),
                     random.choice(colors)
                     )
    )

print(colored_points)