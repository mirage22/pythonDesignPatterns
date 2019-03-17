# Python Basics
# inheritance, encapsulation, abstraction, Polymorphism

class Vehicle():
    def __init__(self):
        print("construct vehicle")


class SportCar(Vehicle):
    def __init__(self, name, ps):
        super().__init__()
        print("construct sport car")
        self.name = name
        self.ps = ps

    def start(self, driverName):
        return "{} drived by {}".format(self.name, driverName)


class A:
    def explore(self):
        print("explore() method from class A")


class B(A):
    def explore(self):
        print("explore() method from class B")


# Client code
# Abstraction.
# Encapsulation.
# Inheritance.
# Polymorphism.

sportCar = SportCar("trabant", 10)

print(sportCar.start("Miro"))

b_obj = B()
a_obj = A()

b_obj.explore()
a_obj.explore()
