# Factory
# =======
# Factory creates an object without exposing the creation logic to the client and refer newly created
# object using a common interface


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def info(self):
        pass


class SportVehicle:
    def info(self):
        return ('Sport car Info')

class TruckVehicle:
    def info(self):
        return ('Truck Info')

class BusVehicle:
    def info(self):
        return ('Bus Info')

class VehicleFactory:
    def createVehicle(self, type):
        return {
            'sport': SportVehicle(),
            'bus': BusVehicle(),
            'truck': TruckVehicle()
        }[type]



### Client Code
factory = VehicleFactory()
x1  = factory.createVehicle("sport")
print(x1.info())
x2 = factory.createVehicle("bus")
print(x2.info())
x3 = factory.createVehicle("truck")
print(x3.info())
