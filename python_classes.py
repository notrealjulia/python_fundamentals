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
#can check if there are letters (there supposed to be 2), if not is new    
class MyClassName:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f'No letters in the string {number}')
        self._number = number
        
    def number(self):
        return self._number
    
