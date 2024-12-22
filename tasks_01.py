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

# 5.task

# 6.task

# 7.task

# 8.task

# 9.task

# 10.task
