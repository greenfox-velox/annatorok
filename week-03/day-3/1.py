# Create a `Circle` class that takes it's radius as constructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        circumference = self.radius * 2 * 3.14
        return circumference

    def get_area(self):
        area = self.radius ** 2 * 3.14
        return area

circleFirst = Circle(6)
print(circleFirst.get_circumferenc())
print(circleFirst.get_area())
