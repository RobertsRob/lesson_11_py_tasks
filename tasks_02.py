# 1.task
# Создайте класс Person с аттрибутами: имя и возраст. Сделайте возраст приватным и создайте геттер и сеттер для него. В методе-сеттере добавьте проверку, что возраст не может быть отрицательным.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным!")

person = Person("Ivan", 25)
print(person.get_age())
person.set_age(30)
print(person.get_age())
person.set_age(-5)


# 2.task
# Создайте класс Employee с приватными аттрибутами __name и __salary. Реализуйте методы-геттеры и сеттеры для изменения имени и зарплаты. В сеттере зарплаты добавьте проверку, чтобы зарплата не была меньше 1000.
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary >= 1000:
            self.__salary = salary
        else:
            print("Зарплата не может быть меньше 1000!")

emp = Employee("John", 1200)
print(emp.get_name(), emp.get_salary())
emp.set_salary(800)
emp.set_salary(1500)

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
