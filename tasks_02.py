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
# Создайте класс BankAccount с приватным атрибутом __balance. Реализуйте методы для пополнения и снятия средств. 
# Проверьте, чтобы нельзя было снять больше, чем есть на балансе. Добавьте метод, возвращающий текущий баланс.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Сумма депозита должна быть положительной.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Невозможно снять указанную сумму.")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())  # 120

# 4.task
# Создайте класс Triangle с приватными атрибутами __a, __b, __c, которые задают длины сторон треугольника.
# Реализуйте методы для установки значений атрибутов и проверки, можно ли составить треугольник с такими сторонами (условие треугольника: сумма двух любых сторон должна быть больше третьей). 
# Если треугольник можно составить, добавьте метод для вычисления его площади по формуле Герона. (https://en.wikipedia.org/wiki/Heron%27s_formula)

from numpy import sqrt

class Triangle:
    def __init__(self, a, b, c):
        self.__a = None
        self.__b = None
        self.__c = None
        self.set_sides(a, b, c)

    def set_sides(self, a, b, c):
        if self.__is_valid_triangle(a, b, c):
            self.__a = a
            self.__b = b
            self.__c = c
        else:
            print("С такими сторонами треугольник невозможен.")

    def __is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a

    def calculate_area(self):
        if not all([self.__a, self.__b, self.__c]):
            print("Стороны треугольника не установлены.")
        else:
            s = (self.__a + self.__b + self.__c) / 2
            return sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

triangle = Triangle(3, 4, 5)
print(triangle.calculate_area())  # 6.0


# 5.task
# 6.task
# 3.task
