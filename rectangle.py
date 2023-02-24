class Rectangle:
    """
    A class representing a rectangle with a width and a height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Computes the area of the rectangle.

        """
        return self.width * self.height

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Compares two rectangles based on their areas.

        """
        return self.area() == other.area()

    def __add__(self, other):
        """
        Computes the sum of two rectangles, creating a new rectangle with an area equal to the sum of the two
        original rectangles' areas.

        """
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width, height)

    def __mul__(self, n):
        """
        Multiplies the rectangle by a number n, creating a new rectangle with an area equal to the original rectangle's
        area multiplied by n.

        """
        width = self.width * n
        height = self.height * n
        return Rectangle(width, height)

r1 = Rectangle(3, 4)
r2 = Rectangle(2, 5)
print(r1 > r2)  # True
print((r1 + r2).area())  # 35.0
print((r1 * 2).area())  # 24.0

