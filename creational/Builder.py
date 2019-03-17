

class Director:
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder._build_part_a()
        self._builder._build_part_b()
        self._builder._build_part_c()


class Builder():
    def __init__(self):
        self.product = Product()

    def _build_part_a(self):
        pass

    def _build_part_b(self):
        pass

    def _build_part_c(self):
        pass


class ConcreteBuilder(Builder):
    def _build_part_a(self):
        print("b1_part_a")
        pass

    def _build_part_b(self):
        print("b1_part_b")
        pass

    def _build_part_c(self):
        print("b1_part_c")
        pass

class ConcreteBuilder2(Builder):
    def _build_part_a(self):
        print("b2_part_a")
        pass

    def _build_part_b(self):
        print("b2_part_b")
        pass

    def _build_part_c(self):
        print("b2_part_c")
        pass


class Product:
    pass


print("Builder Example")
objectBuilder = ConcreteBuilder()
objectBuilder2 = ConcreteBuilder2()
director = Director()

director.construct(objectBuilder)
product1 = objectBuilder.product
director.construct(objectBuilder2)
product2 = objectBuilder2.product

print("product1: %s" % product1)
print("product2: %s" % product2)



