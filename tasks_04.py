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
# Создайте абстрактный класс Speaker с методом speak(). Затем создайте два класса-наследника: Human и Robot, каждый из которых по-своему реализует метод speak(). Создайте список объектов этих классов и вызовите метод speak() для каждого.

class Speaker():
    def speak(self):
        pass

class Human(Speaker):
    def speak(self):
        print("Hello, how are you?")

class Robot(Speaker):
    def speak(self):
        print("Beep boop, I am a robot.")

speakers = [Human(), Robot()]
for speaker in speakers:
    speaker.speak()

# 3.task
# Создайте абстрактный класс Employee с методом salary(). Затем создайте два класса-наследника: FullTimeEmployee и PartTimeEmployee,
# которые реализуют метод salary() по-разному (например, для полной ставки — фиксированная зарплата, для частичной — почасовая, которая рассчитывается путем умнажения проработаных часов на почасовую ставку).

class Employee():
    def salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, hours, hourly_rate):
        self.hours = hours
        self.hourly_rate = hourly_rate

    def salary(self):
        return self.hours * self.hourly_rate

employees = [FullTimeEmployee(5000), PartTimeEmployee(160, 20)]
for employee in employees:
    print(employee.salary())


# 4.task
# Создайте абстрактный класс Movable, который должен содержать метод move(), выводящий информацию о скорости транспортного средства.
# Затем создайте следующие наследующие классы:
# 1. MovableWithEngine — класс для транспортных средств с двигателем. В нем реализуйте метод move(), который сначала выводит информацию о скорости, а затем — о мощности двигателя.
# 2. Bicycle — класс для велосипеда, который не имеет двигателя. В этом классе метод move() должен выводить только скорость.
# 3. Car — класс для автомобиля с двигателем и возможностью перевозить пассажиров. Он должен наследовать MovableWithEngine и использовать его метод move(), при этом добавляя информацию о количестве пассажиров.

class Movable:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        print(f"Переместился co скоростью {self.speed} км/ч!")

class MovableWithEngine(Movable):
    def __init__(self, speed, horse_power):
        super().__init__(speed)
        self.horse_power = horse_power

    def move(self):
        super().move()
        print(f"И c мощностью в {self.horse_power} лошадиных сил!")

class Bicycle(Movable):
    def __init__(self, speed):
        super().__init__(speed)

class Car(MovableWithEngine):
    def __init__(self, speed, horse_power, passenger_count):
        super().__init__(speed, horse_power)
        self.passenger_count = passenger_count

    def move(self):
        super().move()
        print(f"B транспортном средстве {self.passenger_count} пассажиров!")

vehicles = [Bicycle(20, 1), Car(120, 250, 5), Car(200, 600, 2)]
for vehicle in vehicles:
    vehicle.move()



# 5.task

# 6.task

# 7.task

# 8.task

# 9.task

# 10.task
