"""""
def dirty(func):
    def iny():
        return func()+" Nigger"
    return iny

@dirty
def ne():
    return "What's up my"

print(ne())
"""

class Engine:
    def start(self):
        print("Engine starts")
    
    def __str__(self):
        return "This is engine"


class Car:
    def __init__(self):
        self.engine=Engine()


    def __str__(self):
        self.engine.start()
        return "Car starts"




c1=Car()

print(c1)
