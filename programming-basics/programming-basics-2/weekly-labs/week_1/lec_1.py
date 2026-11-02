from math import pi

class Circle:

    def __init__(self, r, x=0, y=0):
        self.x = x
        self.y = y
        self.radius = r

    def calculate_circle_area(self):
        return self.radius ** 2 * pi

    def __str__(self):
        return f"Circle with radius {self.radius} and center in coords ({self.x}, {self.y})."

    def __repr__(self):
        return f"<Circle {self.radius=}, {self.x=}, {self.y=}>"


class Square:

    def __init__(self, a):
        self.side = a

    def calculate_square_area(self):
        return self.side ** 2

    def __str__(self):
        return f"Square with side {self.side}."


def main():
    r, x, y = map(int, input("Enter radius and coords: ").split())
    side = int(input("Enter side: "))

    c = Circle(r, x, y)
    print(c.calculate_circle_area())
    s = Square(side)
    print(s.calculate_square_area())
    print(c)
    print(s)


if __name__ == "__main__":
    main()