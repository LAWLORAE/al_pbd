

import math

def number_check(a): #shield for input type
        number_types = (int, float, complex)
        if not isinstance(a, number_types): 
            return ValueError
        return ' '#to avoid python printing none
        
def exponential(a): #using reduce allows us to take a list of any amount of numbers from user input and only one parameter is needed    
    number_check(a)
    return reduce(lambda x,y: 'nan' if y < 0 else x**y, a)
         
def add(a):
    number_check(a)
    return reduce(lambda x,y: x+y, a)
 
def subtract(a):
    number_check(a)
    return reduce(lambda x, y: x-y, a, b)
        
def multiply(a):
    number_check(a)
    return reduce(lambda x, y: x*y, a)
            
def divide(a):
    number_check(a)
    return reduce(lambda x,y: 'nan' if y == 0 else x/float(y), a)   
         
def sin(a):
    return  map(lambda x: math.sin(x), a)

def cos(a):
    return map(lambda x: math.cos(x), a)
    
def tan(a):
    return map(lambda x: math.tan(x), a)
    
def sqrt(a):
    return map(lambda x: math.sqrt(x), a)

def number_input():
        valid_input = False
        while not valid_input:  
            try: 
                numb_input = raw_input('Enter a list of numbers to calculate: ')
                numbers = list(map(float,numb_input.split())) #take a list of numbers of any length, use the map function to loop over the strings and turn them into intergers, split them at the space, and add to a list
                valid_input = True #once the entry has made it through the except shield, continue to next step
                return numbers
            except:
                print 'Please enter a valid number.'
                               
def list_calculation(a): #Now that we are using the function 'reduce', we can put one list as the parameter and therefore can use one function for calculation.
        valid_input = False
        while not valid_input: 
            try:
                op = int(raw_input(
                "Which operation would you like to use?: \n"
                "[1] Enter 1 for addition. \n"
                "[2] Enter 2 for subtraction. \n"
                "[3] Enter 3 for multiplication. \n"
                "[4] Enter 4 for division. \n"  
                "[5] Enter 5 for exponential. \n"
                "[6] Enter 6 for sin. \n"
                "[7] Enter 7 for cos. \n"
                "[8] Enter 8 for tan. \n"
                "[9] Enter 9 for square root. \n"
                ))
                if op < 0 or op > 9:
                    return ('Please enter number in range 1 to 9.')
                    valid_input = True
                elif op == 1: 
                    return add(a)
                elif op == 2: 
                    return subtract(a)
                elif op == 3: 
                    return mutiply(a)
                elif op == 4:
                    return divide(a)
                elif op == 5: 
                    return exponential(a)    
                elif op == 6:
                    return sin(a)
                elif op == 7:
                    return cos(a)
                elif op == 8:
                    return tan(a)
                elif op == 9:
                    return sqrt(a)      
                valid_input = True
            except: 
                print 'Please enter a valid number.'
    
    
numbers = number_input()
print list_calculation(numbers)

