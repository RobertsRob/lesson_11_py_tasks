
# 1.task
# Создайте класс Book с атрибутами: название, автор, год издания, цена. Реализуйте метод __str__, который выводит строковое представление объекта книги.
class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
    
    def __str__(self):
        return f'"{self.title}" автор - {self.author}, год - {self.year}, цена - {self.price}'

book = Book("1984", "George Orwell", 1949, 500)
print(book)


# 2.task
# Создайте класс Rectangle с аттрибутами длины и ширины. Реализуйте метод area, который вычисляет площадь прямоугольника.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)
print(rect.area())


# 3.task
# Создайте класс Student с аттрибутами: имя, возраст и список оценок. Реализуйте метод average_grade, который вычисляет средний балл.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Ivan", 16, [4, 5, 4, 3, 5])
print(student.average_grade())


# 4.task
# Добавьте в класс Student метод __eq__, который сравнивает студентов по среднему баллу.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

student1 = Student("Ivan", 16, [4, 5, 4, 3, 5])
student2 = Student("Maria", 17, [5, 5, 5, 4, 4])
print(student1 == student2)

# 5.task
# Создайте класс Employee с аттрибутами: имя, должность, зарплата. Реализуйте метод для увеличения зарплаты на процент и метод для вывода полной информации о сотруднике.
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100
    
    def __str__(self):
        return f'{self.name}, {self.position}, зарплата - {self.salary}'

employee = Employee("Alex", "Manager", 50000)
employee.increase_salary(10)
print(employee)

# 6.task

# 7.task

# 8.task

# 9.task

# 10.task
