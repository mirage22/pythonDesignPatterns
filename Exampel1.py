from creational.SingletonMetaclass import Logger

### Client code

logger = Logger()

print("LOGGING1:", logger.log("log1"))
print("LOGGING2:", logger.log("log2"))