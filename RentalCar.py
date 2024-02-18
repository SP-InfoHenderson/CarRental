import datetime

class Car:
    def __init__(self, rego):
        self.rego = rego

class CarRentalController:
    def __init__(self):
        self.__availableCars = [Car("ABC123"), Car("KDJ364") ,Car("SKJ534")]
        self.__rentedCars = []

    def displayAvailableCars(self):
        anyAvailable = False
        for car in self.__availableCars:
            anyAvailable = True
            print("Car rego: " + car.rego)

        if not anyAvailable:
            print("There are no cars available to rent.\r\n")
    
    def rentOutCarHourly(self, carsToBook):
        self.__rentCar(carsToBook, 60)
    
    def rentOutCarDaily(self, carsToBook):
        self.__rentCar(carsToBook, 100)

    def rentOutCarWeekly(self, carsToBook):
        self.__rentCar(carsToBook, 600)

    def __rentCar(self, carsToBook, price):
        if self.__totalCarAvailable() >= carsToBook:
            print("We have completed your booking. Your total price will be $" + str(carsToBook * price) + "\r\n")
            
            i = 0
            while(i < carsToBook):
                self.__rentedCars.append(self.__availableCars.pop())
                i += 1
        else:
            print("Sorry, we don't have " + str(carsToBook) + " cars available to rent.\r\n")

    def __totalCarAvailable(self):
        return len(self.__availableCars)

class CarRentalSystem:
    def __init__(self):
        self.customers = []
        self.carRentalController = CarRentalController()
    
    def start(self):
        self.isRunning = True

        while (True):
            customerOption = input("Please choose from the following options:\r\n1. Show available cars\r\n2. Book car\r\n")

            #Show available stock
            if customerOption == "1":
                self.carRentalController.displayAvailableCars()
            #Show rental options
            elif customerOption == "2":
                periodValid = False
                while(not periodValid):
                    rentalPeriod = input("Please choose the period you would like to book for\r\n1. Hourly\r\n2. Daily\r\n3.Weekly\r\n")
                    if rentalPeriod != "1" and rentalPeriod != "2" and rentalPeriod != "3":
                        print("Invalid option. Please try again.")
                    else:
                        carsToBook = int(input("How many cars would you like to book?"))
                        if rentalPeriod == "1":
                            self.carRentalController.rentOutCarHourly(carsToBook)
                        elif rentalPeriod == "2":
                            self.carRentalController.rentOutCarDaily(carsToBook)
                        elif rentalPeriod == "3":
                            self.carRentalController.rentOutCarWeekly(carsToBook)
                        
                        periodValid = True
            else:   
                print("Invalid option. Please try again.\r\n")

carRentalSystem = CarRentalSystem()
carRentalSystem.start()