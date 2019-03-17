# Facade pattern hides the complexities of the system and provides an interface
# to the client using which the client can access the system. This pattern involves a single class
# which provides simplified methods required by client and delegates calls to methods of existing system classes

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Rectangle:draw()")

class Square(Shape):
    def draw(self):
        print("Square:draw()")

class ShapeMaker:
    def __init__(self):
        self._shapeMap = {
            'rectangle': Rectangle(),
            'square': Square()
        }

    def drawRectangle(self):
        self._shapeMap['rectangle'].draw()

    def drawSquare(self):
        self._shapeMap['square'].draw()


# Client Code
shapeMaker = ShapeMaker()
shapeMaker.drawRectangle()
shapeMaker.drawSquare()
