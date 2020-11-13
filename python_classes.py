#to call flight class import the file name 
#to pass any arguments into the methods in the class we need to define __init__ and assign it to self
#it gets called right after the creation of an object, it doesn't return anything
#_ is used by convention for attributes that should not be modified 
#all methods must call on self

class MyClassName:
    def __init__(self, number):
        self._number = number
        
    def number(self):
        return self._number
    
# if we want to check if the right kind of number has been passed, we can do that in the __init__()
#can check if the first 2 number are digits and raise an error if they are not    
class MyClassName:
    def __init__(self, number):
        if not number[:2].isdigit():
            raise ValueError(f'No letters in the string {number}')
        self._number = number
        
    def number(self):
        return self._number
    
# an example    
class Airplane:
    
    def __ini__(self, registration, model, num_rows, num_seats):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats = num_seats
        
    def resitration(self):
        return self._regitration
    
    def model(self):
        return. self._model
    
    #constructs a seating plan for the plane based on the number of rows and seats per row
    def seating_plan(self):
        return (range(1, self._num_rows + 1), #range is half open, that's why add 1
                "ABCDEFGHJK"[self._num_seats])
    
