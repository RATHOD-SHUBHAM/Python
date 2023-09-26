'''
    Method Overloading: It simply refers to the use of
    many methods with the same name that take various numbers of arguments within a single class
'''

class OverloadingDemo:
    def add(self, x, y):
        print(x+y)

    def add(self, x, y, z):
        print(x+y+z)


obj = OverloadingDemo()
obj.add(2, 3)

'''
     Python doesn't support Method Overloading by default.
     
     Python only remembers the most recent definition of add(self, x, y, z), which takes three parameters in addition to self. 
     As a result, three arguments must be passed to the add() method when it is called. 
     
     To put it another way, it disregards the prior definition of add().


'''