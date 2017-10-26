# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 20:39:09 2017

@author: 10363795
"""
#if in same directory #fro mcalcualtor file in directory import calculator class
from calculator import Calculator 

from pip install mock
import unittest
from mock import patch, MagicMock
from unittest import TestCase


class TestCalculator(unittest.TestCase):
    
    def test_caclulator_multiply(self):
        result = Calculator().multiply(5,5)
        self.assertEqual(25, result)
        result = Calculator().multiply(5,0)
        self.assertEqual(0, result)
        result = Calculator().multiply(5,1)
        self.assertEqual(5, result)
        result = Calculator().multiply(5,0.2)
        self.assertEqual(1, result)
        
    def test_calculator_add(self): 
        result = Calculator().add(5,5)
        self.assertEqual(10, result)
        result = Calculator().add(2,3)
        self.assertEqual(5, result)
        result = Calculator().add(2,0)
        self.assertEqual(2, result)
        result = Caclulator().add('2', '5')
        self.assetEqual('25', result)
        try:
            Calculator().add('2', '5')
            self.fail('should have thrown error') #testing negative case - if code doesn't return error,print warning
        except ValueError:
            pass
        
    def test_calculator_subtract(self): 
        result = Calculator().subtract(5,5)
        self.assertEqual(0, result)
        result = Calculator().subtract(5,3)
        self.assertEqual(2, result)
        result = Calculator().subtract(3,5)
        self.assertEqual(-2, result)
        
    def test_calculator_divide(self): 
        result = Calculator().divide(5,5)
        self.assertEqual(1, result)
        result = Calculator().divide(5,1)
        self.assertEqual(2, result)
        result = Calculator().divide(5,0.2)
        self.assertEqual(25, result)
        result = Calculator().divide(5,4)
        self.assertEqual(1.25, result)
        result = Calculator().divide(5,0)
        self.assertEqual('nan', result)
    
    def test_calculator_exponential(self):
        result = Calculator().exponential(5,2)
        self.assertEqual(25, result)
        result = Calculator().exponential(5,3)
        self.assertEqual(125, result)
        result = Calculator().exponential(10,-9)
        self.assetEqual('nan', result)
        result = Calculator().exponential(5,0)
        self.assetEqual('nan', result)
        
    def test_calculator_number_input(self):
        result =  Calculator().number_input(4,5)
        self.assertEqual([4,5], result)
        result =  Calculator().number_input(4)
        self.assertEqual([4], result)
        try:
            Calculator().number_input('2', '5')
            self.fail('should have thrown error') #testing string - if code doesn't return error,print warning
        except ValueError:
            pass
    
    def test_calculator_sqr(self):
        result = Calculator().sqr(7)
        self.assertEqual(2.64575131106, result)
        result = Calculator().sqr(-5)
        self.assertEqual('nan', result)
        result = Calculator().sqr(0)
        self.assertEqual(0, result)

    def test_calculator_sin(self):
        result = Calculator().sin(7)
        self.assertEqual(0.656986598719, result)
        result = Calculator().sin(-5)
        self.assertEqual(0.958924274663, result)
        result = Calculator().sin(0)
        self.assertEqual(0, result)     

    def test_calculator_cos(self):
        result = Calculator().cos(7)
        self.assertEqual(0.753902254343, result)
        result = Calculator().cos(-5)
        self.assertEqual(0.283662185463, result)
        result = Calculator().cos(0)
        self.assertEqual(1, result)
    
    def test_calculator_tan(self):
        result = Calculator().tan(7)
        self.assertEqual(0.871447982724, result)
        result = Calculator().tan(-5)
        self.assertEqual(3.38051500625, result)
        result = Calculator().tan(0)
        self.assertEqual(0, result)    
            
    @patch('Calculator.operation_1number', return_value = 1)     
    def test_calculator_op1_sin(self, input):
        result =  Calculator().sin(5)
        self.assertEqual(result, Calculator().sin(5))    
        
    @patch('Calculator.operation_1number', return_value = 2)     
    def test_calculator_op1_cos(self, input):
        result =  Calculator().cos(5)
        self.assertEqual(result, Calculator().cos(5))    
        
    @patch('Calculator.operation_1number', return_value = 3)     
    def test_calculator_op1_tan(self, input):
        result =  Calculator().tan(5)
        self.assertEqual(result, Calculator().tan(5))    
    
    @patch('Calculator.operation_1number', return_value = 4)     
    def test_calculator_op1_sqrt(self, input):
        result =  Calculator().sqrt(5)
        self.assertEqual(result, Calculator().sqrt(5))    
        
    @patch('Calculator.operation_2numbers', return_value = 1)     
    def test_calculator_op1_add(self, input):
        result =  Calculator().add(5,5)
        self.assertEqual(result, Calculator().add(5,5))    
    
    @patch('Calculator.operation_2numbers', return_value = 2)     
    def test_calculator_op1_subtract(self, input):
        result =  Calculator().subtract(5,5)
        self.assertEqual(result, Calculator().subtract(5,5))  
        
    @patch('Calculator.operation_2numbers', return_value = 3)     
    def test_calculator_op1_multiply(self, input):
        result =  Calculator().multiply(5,5)
        self.assertEqual(result, Calculator().multiply(5,5))
        
    @patch('Calculator.operation_2numbers', return_value = 4)     
    def test_calculator_op1_divide(self, input):
        result =  Calculator().divide(5,5)
        self.assertEqual(result, Calculator().divide(5,5))
    
    @patch('Calculator.operation_2numbers', return_value = 5)     
    def test_calculator_op1_exp(self, input):
        result =  Calculator().exponential(5,5)
        self.assertEqual(result, Calculator().exponential(5,5))
        
        
    