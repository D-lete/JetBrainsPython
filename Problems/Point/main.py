class Point:
    pass
    points = []

    def __init__(self):
        point = float(input(self)), float(input(self))
        Point.points.append(point)

    def dist(self):
        float(((Point.points.pop(0) - Point.points.pop(2)) ^ 2 + (Point.points.pop(1) - Point.points.pop(3)) ^ 2) ^ .5)
