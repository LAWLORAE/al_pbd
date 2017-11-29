

from car import Car, PetrolCar, DieselCar, ElectricCar, HybridCar
from dealership import Dealership

system = Dealership()
system.create_stock('dealership.csv') #load stock into system from csv

rental_pool = system.rental_pool() #create class instances and put them in a rental_pool dictionary

print system.rent_or_return() #rent or return user input function



  