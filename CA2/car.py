# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self, colour, model, year, reg):
        self.__colour = colour
        self.__mileage = 0
        self.__model = model
        self.__year = year
        self.__reg = reg

    def getColour(self):
        return self.__colour

    def getModel(self):
        return self.__model
    
    def getYear(self):
        return self.__year

    def getReg(self):
        return self.__reg

    def setColour(self, colour):
        self.__colour = colour
        return self.__colour

    def setModel(self, model):
        self.__model = model
        return self.__model
          
    def setYear(self, year):
        self.__year = year
        return self.__year
        
    def setReg(self, reg):
        self.__reg = reg
        return self.__reg
        
    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage

    def __repr__(self):
        return self.__reg + ' ' + self.__colour + ' ' + str(self.__mileage) + ' ' + self.__model + ' ' + str(self.__year)

class PetrolCar(Car):

    def __init__(self, colour, model, year, reg, mileage, engineSize, numberCylinders):
        Car.__init__(self, colour, model, year, reg)
        self.__mileage = mileage
        self.engineSize = engineSize
        self.__numberCylinders  = numberCylinders
        
    def getMileage(self):
        return self.__mileage
        
    def getEngineSize(self):
        return self.__enginesize 
        
    def getNumberCylinders(self):
        return self.__numberCylinders
        
    def setMileage(self, value): 
        self.__mileage = value
        return self.__mileage
        
    def setEngineSize(self, value):
        self.__engineSize = value
        return self.__engineSize
        
    def setNumberCylinders(self, value):
        self.__numberCylinders = value
        return self.__numberCylinders
        
class DieselCar(Car):

    def __init__(self, colour, model, year, reg, mileage, engineSize, NumberCycles, combustion):
        Car.__init__(self, colour, model, year, reg)
        self.__mileage = (mileage)
        self.__engineSize = (engineSize)
        self.__combustion = (combustion)
        self.__numberCycles = (NumberCycles)
        
    def getMileage(self):
        return self.__mileage
        
    def getEngineSize(self):
        return self.__enginesize 
        
    def getcombustion(self):
        return self.__combustion
    
    def getNumberCycles(self, value):
        self.__numberCycles
        
    def setMileage(self, value):
        self.__mileage = value
        return self.__mileage
        
    def setEngineSize(self, value):
        self.__engineSize = value
        return self.__engineSize
        
    def setcombustion(self, value):
        self.__combustion = value
        return self.__combustion
    
    def setNumberCycles(self, value):
        self.__numberCycles = value
        return self.__numberCycles
      

#sub-classes: call main class in brackets as a parameter
class ElectricCar(Car):
    
    def __init__(self, colour, model, year, reg, range, motor, battery):
        Car.__init__(self, colour, model, year, reg)
        self.__range = (range)
        self.__motor =  (motor)
        self.__battery = (battery)
    
    def getRange(self):
        return self.__range
    
    def getMotor(self):
        return self.__motor
    
    def getBattery(self):
        return self.__battery
           
    def setRange(self, value):
        self.__range = value
        return self.__range
           
    def setMotor(self, value):
        self.__motor = value
        return self.__motor
        
    def setbattery(self, value):
        self.__battery = value
        return self.__battery
               
    def UpgradeBatteryPack(self, value):
        self.__battery = self.__battery + newdistance
        return self.__battery
   
   
class HybridCar(Car):
    
    def __init__(self, colour, model, year, reg, motor, powertrain):
        Car.__init__(self, colour, model, year, reg)
        self.__motor =  (motor)
        self.__powertrain = (powertrain)
    
    def getMotor(self):
        return self.__motor
    
    def getPowerTrain(self):
        return self.__powertrain
        
    def setMotor(self, value):
        self.__motor = value
        return self.__motor
        
    def setPowerTrain(self, value):
        self.__powertrain = value
        return  self.__powertrain
               
    def UpgradeBatteryPack(self, value):
        self.__battery = self.__battery + newdistance
        return self.__battery

