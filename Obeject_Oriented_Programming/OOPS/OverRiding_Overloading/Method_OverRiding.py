'''
    When a method with the same name and arguments is used in both a derived class and a base or super class,
    we say that the derived class method "overrides" the method provided in the base class.
'''

class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")
        super().call_me()

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()