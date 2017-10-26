


from calculator import Calculator
import math

Casio = Calculator()

numbers = Casio.number_input()

if len(numbers) == 1:#if length of list is equal to 1...
    print Casio.operation_1number(numbers[0])   #run operation one, which will offer sin, cos, and tan, on first index (in this case, the only index)
else: 
    print Casio.operation_2numbers(numbers[0],numbers[1]) #if list is longer than 1, run op2 function on first and second index. if list is longer than 2, tough luck as a limit of 2 was specified

