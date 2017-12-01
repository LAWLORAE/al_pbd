import unittest

from car import Car, PetrolCar, DieselCar, ElectricCar, HybridCar
from dealership import Dealership

"""
red_car = Car()
print 'Colour ' + red_car.getColour()

red_car.paint('red')
print 'Colour ' + red_car.getColour()


print 'Engine Size ' + red_car.engineSize
red_car.engineSize = '3.9'
print 'Engine Size ' + red_car.engineSize
"""

# test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        
    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        
    

if __name__ == '__main__':
    unittest.main()
    
class TestHybridCar(unittest.TestCase):

    def test_car_setUp(self):
        self.car = HybridCar()

    def test_car_setMotor(self):
        self.assertEqual(0, self.car.getMotor())
        self.car.setMotor(3)
        self.assertEqual(3, self.car.getMotor())
        
    def test_car_setPowerTrain(self):
        self.assertEqual(0, self.car.getPowerTrain())
        self.car.setPowerTrain(3)
        self.assertEqual(3, self.car.getPowerTrain())
               
    def test_car_UpgradeBatteryPack(self):
        self.assertEqual(1, self.car.UpgradeBatteryPack())
        self.car.UpgradeBatteryPack(2)
        self.assertEqual(3, self.car.UpgradeBatteryPack())  
    
class TestPetrolCar(unittest.TestCase):
   
    def setUp(self):
        self.car = PetrolCar()
    
    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
    
    def test_car_engineSize(self):
        self.assertEqual(0, self.car.getEngineSize())
        self.car.setEngineSize(15)
        self.assertEqual(15, self.car.getEngineSize())
        
    def test_car_numberCylinders(self):
        self.assertEqual(0, self.car.getNumberCylinders())
        self.car.setNumberCylinders(3)
        self.assertEqual(3, self.car.getNumberCylinders())
    
class TestElectricCar(unittest.TestCase):    
    
    def setUp(self):
        self.car = ElectricCar()
    
    def test_car_setcombustion(self, value):
        self.assertEqual(0, self.car.getcombustion())
        self.car.setcombustion(3)
        self.assertEqual(3, self.car.getcombustion())
    
    def test_car_setNumberCycles(self, value):
        self.assertEqual(0, self.car.getNumberCycles())
        self.car.setNumberCycles(3)
        self.assertEqual(3, self.car.getNumberCycles())
    
    
class TestDieselCar(unittest.TestCase):    
    
    def test_setUp(self):
        self.car = DieselCar()
    
    def test_setRange(self, value):
        self.assertEqual(0, self.car.getRange())
        self.car.setRange(3)
        self.assertEqual(3, self.car.getRange())
    
           
    def test_setMotor(self, value):
        self.assertEqual(0, self.car.getMotor())
        self.car.setMotor(3)
        self.assertEqual(3, self.car.getMotor())
    
        
    def test_setbattery(self, value):
        self.assertEqual(0, self.car.getbattery())
        self.car.setbattery((3)
        self.assertEqual(3, self.car.getbattery(())
                 
    def test_UpgradeBatteryPack(self, value):
        self.assertEqual(1, self.car.UpgradeBatteryPack())
        self.car.UpgradeBatteryPack(2)
        self.assertEqual(3, self.car.UpgradeBatteryPack())  

 
class TestDealership(unittest.TestCase):         
    def test_stock_list 
        list = self.car.create_stock('dealership.csv') #check if there is a class object in a list
        for e in list:
            if isinstance(e, list):
                pass
            else: 
                self.fail('should be a list.') #testing string - if code doesn't return error,print warning
  
            

