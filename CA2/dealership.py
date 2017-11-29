
from car import Car, PetrolCar, DieselCar, ElectricCar, HybridCar

class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []
        self.reg_dict = {}
        self.rental_list = [] #create a rental list to fill with all car, reg dictionaries
    
    def GetRental_list(self):
        return self.rental_list
       
    def import_stock(self, file_name): #import car csv
        stock = open(file_name)
        stocklines = stock.readlines() #read all lines into a string
        return map(lambda x: x.strip().split(','), stocklines) #map or loop over the rows, create seperate lists for each one w/ split function
        
    def create_stock(self, file_name): #function to turn each list into an object of a relevant car class (petrol, diesel, etc)
        stock = self.import_stock(file_name) 
        for values in stock:
            if values[0] == 'Petrol': #if the first word in the list is petrol, import the PetrolCar class instances and assign them to values, mapped onto the class functions 
                self.petrol_cars.append(PetrolCar(values[1], values[2], values[3], values[4], values[5], values[6], values[7]))  
            if values[0] == 'Diesel':
                self.diesel_cars.append(DieselCar(values[1], values[2], values[3], values[4], values[5], values[6], values[8], values[9]))     
            if values[0] == 'Electric':
                self.electric_cars.append(ElectricCar(values[1], values[2], values[3], values[4], values[10], values[11], values[12])) 
            if values[0] == 'Hybrid':
                self.hybrid_cars.append(HybridCar(values[1], values[2], values[3], values[4], values[12], values[13])) 
        
    def reg_plate(self, car_list): #create function which generates a unqiue reg plate key, for every car in a car list 
        reg_dict = {} 
        for car in car_list: #for every car in car list
            reg_dict[car.getReg()] = car #create a reg plate key, with the value as the instances of the car object
        return reg_dict 

    def rental_pool(self):#assign reg plate function to all car lists, and create rental pool, where we can select cars and identify reg
        self.rental_list.extend([self.reg_plate(self.petrol_cars), self.reg_plate(self.diesel_cars), self.reg_plate(self.electric_cars), self.reg_plate(self.hybrid_cars)])
        return self.rental_list
        
    def stock_check(self):#create stock list, as masterlist, to check full class instance details of incoming reg plates for cars being returned
        return [self.reg_plate(self.petrol_cars), self.reg_plate(self.diesel_cars), self.reg_plate(self.electric_cars), self.reg_plate(self.hybrid_cars)]
    
    def rent(self, pool, request):
        cust_order = [] #create list for customer rental cars
        stock = len(pool)
        if stock < request: #if stock of car list is less than rental amount requested
            return 'Not enough cars in stock'  
        total = 0
        while total < request:#until request amount reaches 0 
            pool.popitem()
            cust_order.append(pool.popitem()) #pop last item/s from dictionary
            total = total + 1
        for tuple in cust_order: #for every rented car in list
            print 'Your reg number is' ' ' + str(tuple[0]) +  '.' 
        return 'Please use this when returning the rental.' #return the first value, which is the reg
    
    def return_car(self, cust_pool, request):
        stock = self.stock_check() #create a variable of full stock list to check return reg
        valid_input = False
        while not valid_input:
            try:
                total = 0
                while total < request: #while request is more than 0 repeat below steps
                    reg = raw_input(str('Please enter the 9 digit reg plate number you would like to return. \n'))
                    if len(reg) != 9:
                        print ('Please enter 9 digits.')
                        valid_input = True
                    else:
                        car = stock[0].get(reg) #find the car from the reg key with get function
                        cust_pool[car.getReg()] = car #turn the class instance from the stock list back into a dictionary k,v, pair, and add the car back to the right car pool
                        valid_input = True               
                        print  'Your return has been registered.'
                    total = total + 1
                return ' '
            except: 
                return ('Please enter a correct value.\n')    

    def choose_cartype(self):
        choice = ['p', 'd', 'e', 'h']
        valid_input = False
        while not valid_input:
            car_type = raw_input('What type would you like?\n' 
                         'Enter p for petrol. \n' 
                         'Enter d for diesel.\n' 
                         'Enter e for electric.\n' 
                         'Enter h for hybrid.\n').lower()
            if car_type not in choice:
                print ('Please choose from one of four options listed.\n')
            else:
                return car_type
                valid_input = True
      
    def rent_or_return(self):
        valid_input = False
        while not valid_input:
            try:
                answer = raw_input(str('Would you like to rent or return a car? rent/return \n')).lower()
                if answer == 'rent':
                    print self.rental_interface(self.rent) #put rent function into user interface
                    valid_input = True
                elif answer == 'return':
                    return self.rental_interface(self.return_car) #put return car function into user interface
                    valid_input = True
            except:
                return ('Please choose from one of two options listed.\n')
            
    def rental_interface(self, cust_action): #cust action will always be rent or return, and will be populated by the rent or return input function
        rental_list = self.rental_pool()
        valid_input = False
        while not valid_input:
            try:
                request = int(raw_input('How many? \n'))
                valid_input = True
                car_type = self.choose_cartype() 
                if car_type == 'p':                  
                    return cust_action(self.rental_list[0], request) #The petrol car list is the first index in the rental pool - hence rental[0]
                if car_type == 'd':                  
                    return cust_action(self.rental_list[1], request) 
                if car_type == 'e':                  
                    return cust_action(self.rental_list[2], request)
                if car_type == 'h':                  
                    return cust_action(self.rental_list[3], request)
                elif answer == 'n':
                    return "Thankyou! You have chosen to quit this program."
                    valid_input = True       
            except:
                return "Please enter a valid number."  

    

    