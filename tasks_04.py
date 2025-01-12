# 1.task
# Создайте абстрактный класс Shape с абстрактным методом area(). Затем создайте два класса-наследника: Circle и Rectangle, которые реализуют метод area(). 
# Создайте список объектов разных классов и вызовите метод area() для каждого.

class Shape():
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())

# 2.task

# 3.task

# 4.task

# 5.task

# 6.task

# 7.task

# 8.task

# 9.task

# 10.task
