'''
    Prevent the program fron crashing
    Try, Except: https://docs.python.org/3/tutorial/errors.html
    Exceptions: https://docs.python.org/3/library/exceptions.html#bltin-exceptions
'''
values = [10, 5, 6, 0, 9, 8, 2]

for val in values:
    try:
        '''
            Code where you might want to catch the error
        '''
        print(10/ val)
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        '''
        If try works successfully, Then Execute this part
        '''
        print(" This works")
    finally:
        '''
            Run no matter what happen in try except
        '''
        print(10 * 10)


