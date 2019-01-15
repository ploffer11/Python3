import math 

square = [(1,1), (1,2), (2,2), (2,1)]

# Not OOP

def distance(p1, p2):
    return math.sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )

def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i+1])
    return perimeter

# OOP

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def distance(self, p2):
        return math.sqrt(
            (self.x - p2.x)**2 + (self.y - p2.y)**2
        )

class Polygon:
    def __init__(self, points = None):
        points = points if points else []
        self.vertices = []
        for point in points:
            if isinstance(point, tuple):
                point = Point(*point)
            self.vertices.append(point)

    def add_point(self, point):
        self.vertices.append(point)

    def perimeter(self):
        perimeter = 0
        for i in range(len(self.vertices)):
            perimeter += self.vertices[i].distance(self.vertices[i-1])
        return perimeter

square = Polygon([(1,1), (1,2), (2,2), (2,1)])
#square.add_point(Point(1, 1))
#square.add_point(Point(1, 2))
#square.add_point(Point(2, 2))
#square.add_point(Point(2, 1))

print( square.perimeter() )
print( square.vertices )