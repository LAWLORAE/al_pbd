# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:14:36 2017

@author: 10363795

"""
import unittest
import math

class Calculator(object):


    def number_check(self, x, y): #shield for input type
        number_types = (int, float, complex)
        if not isinstance(x, number_types) and isinstance(y, number_types): 
            return ValueError
        return ' '#to avoid python printing none
      
    def exponential(self, x, y):
        if y < 0:
            return 'nan'
        elif self.number_check(x,y):
            answer = (x**y)
            first_line = '{} ^ {} = '.format(x,y) + '\n' + str(answer)
            return first_line 
    
    def add(self, x, y):
        self.number_check(x,y)
        answer = (x+y)
        first_line = '{} + {} = '.format(x,y) + '\n' + str(answer)
        return first_line
    
    def subtract(self, x, y):
        self.number_check(x,y)
        answer = (x-y)
        first_line = '{} - {} = '.format(x,y) + '\n' + str(answer)
        return first_line 
        
    def multiply(self, x, y):
        self.number_check(x,y)
        answer = (x*y)
        first_line = '{} x {} = '.format(x,y) + '\n' + str(answer)
        return first_line 
            
    def divide(self, x, y):
        if y == 0:
             return 'nan'
        elif self.number_check(x,y):
            answer = (x / float(y))
        first_line = '{} / {} = '.format(x,y) + '\n' + str(answer)
        return first_line
         
    def sin(self, x):
        answer = (math.sin(x))
        first_line = 'sin(x) = '.format(x) + '\n' + str(answer)
        return first_line
    
    def cos(self, x):
        answer = (math.cos(x))
        first_line = 'cos(x) = '.format(x) + '\n' + str(answer)
        return first_line

    def tan(self, x):
         number_check(self, x)
         return math.tan(x)
    
    def sqrt(self, x):
        return math.sqrt(x)

    def number_input(self):
        valid_input = False
        while not valid_input:  
            try: 
                numb_input = raw_input('Enter up to two numbers to calculate: ')
                numbers = list(map(float,numb_input.split())) #take up to two numbers, use the map function to loop over the strings and turn them into intergers, split them at the space, and add to a list
                valid_input = True #once the entry has made it through the except shield, continue to next step
                return numbers
            except:
                print 'Please enter a valid number.'
                

    def operation_2numbers(self,x,y): #A function has a definitive number of parameters. Need two functions to cover one and two-number inputs.
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
                ))
                if op < 0 or op > 5:
                    return ('Please enter number in range 1 to 5.')
                    valid_input = True
                elif op == 1: 
                    return self.add(x,y)
                elif op == 2: 
                    return self.subtract(x,y)
                elif op == 3: 
                    return self.mutiply(x,y)
                elif op == 4:
                    return self.divide(x,y)
                elif op == 5: 
                    return self.exponential(x,y)
                valid_input = True
            except: 
                print 'Please enter a valid number.'
    
    def operation_1number(self, x):
        valid_input = False
        while not valid_input: 
            try:
                op = int(raw_input(
                "Which operation would you like to use?: \n"
                "[1] Enter 1 for sin. \n"
                "[2] Enter 2 for cos. \n"
                "[3] Enter 3 for tan. \n"
                "[4] Enter 4 for square root. \n"
                ))
                if op < 0 or op > 4:
                    return ('Please enter number in range 1 to 4.')
                    valid_input = True
                elif op == 1:
                    return self.sin(x)
                elif op == 2:
                    return self.cos(x)
                elif op == 3:
                    return self.tan(x)
                elif op == 4:
                    return self.sqrt(x)
            except: 
                print 'Please enter a valid number.'   
    
if __name__ == '_main_':
    unittest.main() 

'''
        
#use test so we don't have to run print script to test all the time
calculator = Calculator()
print(calculator.add(5, 5))
print(calculator.add(3,2))

print(calculator.subtract(5,5))
print(calculator.subtract(3,2))

#test to tell us if working correctly

'''