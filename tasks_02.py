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
