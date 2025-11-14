def changecase(func):
    def myinner():
        return func().upper()
    return myinner


@changecase
def myfunction():
    return "Hello Sally"

print(myfunction())


def changecaser(func):
    def inner():
        return func().lower()
    return inner

@changecaser
def do_up():
    return "HELLO WORLD"

print(do_up())    


def dirty(func):
    def iny():
        return func()+" Nigger"
    return iny

@dirty
def ne():
    return "What's up my"

print(ne())


