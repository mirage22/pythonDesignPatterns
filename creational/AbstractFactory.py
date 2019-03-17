# AbstractFactory
# =======
# AbstractFactory sometimes called factory of factories. An interface is responsible
# for creating a factory of related object without explicitly specifying their classes.
# Each generated factory can five the objects as per Factory pattern.

from abc import ABC, abstractmethod

class VehicleFactory(ABC):
    @abstractmethod
    def createPkw(self):
        pass
    @abstractmethod
    def createLkw(self):
        pass

class ManFactory(VehicleFactory):
    def createPkw(self):
        return ManTransporters()
    def createLkw(self):
        return ManTruckAndBus()

class VwFactory(VehicleFactory):
    def createPkw(self):
        return VwVehicles()
    def createLkw(self):
        return VwTrucks()

class Vehicles(ABC):
    @abstractmethod
    def offers(self):
        pass

class ManTransporters(Vehicles):
    def offers(self):
        print('MAN transporters')

class ManTruckAndBus(Vehicles):
    def offers(self):
        print('MAN Truck & Bus')

class VwVehicles(Vehicles):
    def offers(self):
        print("VW vehicle: Golf, Passat etc.")

class VwTrucks(Vehicles):
    def offers(self):
        print('VW small trucks...')


class VehicleProduction:
    def produce(self):
        abstract_factory = ManFactory()
        lkw_factory = abstract_factory.createLkw()
        lkw_factory.offers()


        abstract_factory = VwFactory()
        pkw_factory = abstract_factory.createPkw()
        pkw_factory.offers()

# Client code
production = VehicleProduction()
production.produce()