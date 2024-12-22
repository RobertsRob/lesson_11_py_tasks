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

# 3.task

# 4.task

# 5.task

# 6.task

# 7.task

# 8.task

# 9.task

# 10.task
