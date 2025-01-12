# 1.task
# Создайте два класса: Shape и Rectangle. Класс Shape должен иметь метод area, который возвращает 0, а класс Rectangle должен наследовать Shape и переопределить метод area, чтобы вычислять площадь прямоугольника по формуле width * height.

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rectangle = Rectangle(5, 10)
print(rectangle.area())  # 50


# 2.task
# Создайте два класса: Worker и Student. Класс Worker должен иметь метод work, который выводит сообщение о том, что работник выполняет свою работу. Класс Student должен иметь метод study, который выводит сообщение о том, что студент учится. 
# Создайте класс WorkingStudent, который будет наследовать и от Worker, и от Student. Переопределите метод work так, чтобы он выводил и информацию о работе, и о учебе.

class Worker:
    def work(self):
        print("Working on the job.")

class Student:
    def study(self):
        print("Studying for exams.")

class WorkingStudent(Worker, Student):
    def work(self):
        super().work()
        self.study()

working_student = WorkingStudent()
working_student.work()


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
