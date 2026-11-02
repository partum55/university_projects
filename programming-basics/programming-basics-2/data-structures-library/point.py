# Point Class Implementation

from math import cos, sin, radians

class Point:
    """Represents a point in two-dimensional geometric coordinates"""
    
    def __init__(self, x=0, y=0):
        """Initialize the position of a new point. The x and y coordinates can be
        specified. If they are not, the point defaults to the origin."""
        self.move(x, y)
    
    def move(self, x, y):
        """Move the point to a new location in 2D space."""
        self._x = x
        self._y = y
    
    def rotate(self, beta, other_point):
        """Rotate point around other point"""
        dx = self.get_x() - other_point.get_x()
        dy = self.get_y() - other_point.get_y()
        beta = radians(beta)
        xpoint3 = dx * cos(beta) - dy * sin(beta)
        ypoint3 = dy * cos(beta) + dx * sin(beta)
        xpoint3 = xpoint3 + other_point.get_x()
        ypoint3 = ypoint3 + other_point.get_y()
        return self.move(xpoint3, ypoint3)
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
        
    def __str__(self):
        return f"Point({self._x}, {self._y})"
