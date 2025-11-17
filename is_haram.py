class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

        #getter

    def get_name(self):
        return self.__name
        
        #setter

    def set_name(self,new_name):
            self.__name=new_name

    def get_age(self):
            return self.__age

    def set_age(self, new_age):

        if new_age>0:
                self.__age=new_age
        else:
                print("Yosh musbat bo'lishi kerak")


p=Person("Alimjan",19)

print(p.get_name())
p.set_age(30)
print(p.get_age())


p.set_age(-5)