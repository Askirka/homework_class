class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


rectangle1 = Rectangle(5, 8)
print(f"Площадь прямоугольника: {rectangle1.get_area()}")
print(f"Периметр прямоугольника: {rectangle1.get_perimeter()}")
print(f"Прямоугольник является квадратом: {rectangle1.is_square()}")

