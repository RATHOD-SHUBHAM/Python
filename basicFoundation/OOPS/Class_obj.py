'''
    class: A class is a collection of instance variables and related methods that define a particular object type.
    You can think of a class as an object's blueprint or template.

    Attributes: Attributes are the names given to the variables that make up a class.

    Object: A class instance with a defined set of properties is called an object.

'''

class Book:
    '''
        The __init__ special method, also known as a Constructor,
        Constructor is used to initialize the Book class with attributes such as title, quantity, author, and price.
    '''
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    '''
        In Python, a special method is a defined function that starts and ends with two underscores 
        and is invoked automatically when certain conditions are met.
    '''

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


if __name__ == '__main__':
    '''
        This class can be instantiated to any number of objects. 
    '''
    book1 = Book('Book 1', 12, 'Author 1', 120)
    book2 = Book('Book 2', 18, 'Author 2', 220)
    book3 = Book('Book 3', 28, 'Author 3', 320)

    print(book1)
    print(book2)
    print(book3)