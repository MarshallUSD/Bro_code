"""
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}sm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new):
        if new> 0:
            self._width = new
        else:
            print("New width must be greater than 0")

    @height.setter

    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("New height must be greater than 0")

    @width.deleter

    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(3,4)

rectangle.width = 7
rectangle.height = 8

del rectangle.width
del rectangle.height

#print(rectangle.width)
#print(rectangle.height)

#decorators = A function that extends the behaviors of another function

def add_sprinkles(func):
    def wrapper():
        print("*Adding Sprinkles🎇*")
        func()
    return wrapper

@add_sprinkles
def ice_cream():
    print("Here is yours ice cream🍨")

ice_cream()
"""
def add_vegetables(func):
    def wrapper(*args, **kwargs):
        print("Adding vegetables to soup🍅🥦🥬🥒")
        func(*args, **kwargs)
    return wrapper

def add_spices(func):
    def wrapper(*args, **kwargs):
        print("Adding spices...🧂")
        func(*args, **kwargs)
    return wrapper
@add_vegetables
@add_spices
def soup_cooking(flavor):
    print(f"Here is your {flavor} soup 🍲🍲🍲")

soup_cooking("Yalpizli")