import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.move(x, y)

    def move(self, x, y):
        self.x, self.y = x, y
    
    def calculate_distance(self, other_point):
        return math.sqrt( 
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2 
        )

    def reset(self):
        self.x, self.y = 0, 0
    
p = Point(3, 5)    
p1 = Point()
p2 = Point()

p1.reset()
p2.move(5, 0)

print( p1.calculate_distance( p2 ) )

p1.move(3,4)
print( p1.calculate_distance( p2 ) )



