class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def description(self):
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")


rect = Rectangle(4, 3)
rect.description()
