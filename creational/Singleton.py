# Singleton
# ========
# Singleton is responsible to create an object while making sure that only single
# object gets created. Class provides a way to access its only object which can
# be accessed directly without need to instantiate the object of the class

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

# Client code
# s1 and s2 refers to the same object
s1 = Singleton()
print("First Call s1:", s1)

s2 = Singleton()
print ("Second call s2: ", s2)