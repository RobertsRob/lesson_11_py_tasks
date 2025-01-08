# 1.task

# 2.task

# 3.task

# 4.task

# 5.task

# 6.task

# 7.task

# 8.task

# 9.task

# 10.task



/////////////////////////////////////////////////////// na dorabotku:

# 3.task
# Создайте класс Shape, в котором реализуйте метод area. Создайте класс Circle, который наследует от Shape и переопределяет метод area для вычисления площади круга.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())

# 4.task
# Создайте класс Person, который имеет метод для изменения имени. Наследуйте от этого класса класс Employee, который добавляет аттрибут для зарплаты и переопределяет метод для изменения имени с добавлением приветствия.
class Person:
    def __init__(self, name):
        self.name = name
    
    def change_name(self, new_name):
        self.name = new_name

class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    
    def change_name(self, new_name):
        super().change_name(new_name)
        print(f"Привет, {self.name}!")

emp = Employee("John", 5000)
emp.change_name("Alex")
