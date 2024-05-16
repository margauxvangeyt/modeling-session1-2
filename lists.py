import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

randon_points =[Point(random.randint(1,100), random.randint(1,100)) for _ in range(5)]

for i, point in enumerate(randon_points, start=1):
    print(f"Point {i}: ({point.x}, {point.y})")
