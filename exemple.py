class Point:
    color = 'red'
    circle = 2

    def __init__(self, a, b):
        self.x = a
        self.y = b
    def __del__(self):
        print('Удаление экземпляра: ' + str(self))
    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

pt = Point(1, 2 )
print(pt.__dict__)

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

blue_car = Car(color='blue', mileage=20_000)
red_car = Car(color='red', mileage=30_000)
for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,} miles")

    # position, name, age, level, salary
    se1 = ["Sofware engineer", "Kiril", 23, "junior", 5000]
    se2 = ["Sofware engineer", "Olga", 30, "senior", 7000]
    d1 = ["Designer", "Phillip"]

# Class
class SofwareEngineer:
    # class attribute
    alias = "Keyboard Magician"

    def __init__(self, name, age, level, salary):
            # instance attributes
            self.name = name
            self.age = age
            self.level = level
            self.salary = salary

    # instance method
    def code(self):
        print(f"{self.name} is writing code")

# instance
se1 = SofwareEngineer("Kiril", 23, "junior", 5000)
se2 = SofwareEngineer("Olga", 30, "senior", 7000)
se1.code()
se2.code()
print(SofwareEngineer.alias, SofwareEngineer.alias)