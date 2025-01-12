# 1.task
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
# Создайте два класса: EmailSender (отправка email) и SMSSender (отправка SMS). 
# Затем создайте класс Notification, который будет наследовать оба этих класса и использовать оба метода для отправки уведомлений (одновременно отправляя email и SMS).

class EmailSender:
    def send_email(self, message):
        print(f"Email sent: {message}")

class SMSSender:
    def send_sms(self, message):
        print(f"SMS sent: {message}")

class Notification(EmailSender, SMSSender):
    def send_notification(self, message):
        self.send_email(message)
        self.send_sms(message)

notification = Notification()
notification.send_notification("You have a new message!") 

# 4.task
# Создайте два класса - Vehicle, который имеет атрибут speed и метод drive(), который выводит что машина едет с определенной скоростью. 
# А также класс ElectricVehicle, который наследует Vehicle и добавляет атрибут battery_level и метод charge(), который восполняет battery_level до 100 процентов.
# В классе ElectricVehicle переопределите метод drive(), чтобы сначала проверять уровень заряда батареи перед тем, как ехать и при езде отнимать 10 процентов заряда.

class Vehicle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self):
        print(f"Driving at {self.speed} km/h")

class ElectricVehicle(Vehicle):
    def __init__(self, speed, battery_level):
        super().__init__(speed)
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = 100
        print("Charging completed. Battery level is now 100%.")

    def drive(self):
        if self.battery_level > 0:
            super().drive()
            self.battery_level -= 10
            print(f"Battery level is now {self.battery_level}%.")
        else:
            print("Battery is empty. Please charge the vehicle.")

ev = ElectricVehicle(60, 50)
ev.drive()
ev.charge()


