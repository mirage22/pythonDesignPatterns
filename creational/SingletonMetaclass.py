# Singleton with meta class
# ======
# see Singleton.py

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def log(cls, text):
        return ("some:", cls, "text:%s" % (text))

    pass


# Client code
# both loggers refers to the same object
# ======
logger1 = Logger()
logger2 = Logger()

print(logger1.log('something'))
print(logger1, logger2)
