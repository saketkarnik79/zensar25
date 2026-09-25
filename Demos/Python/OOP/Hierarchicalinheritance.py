class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")


car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()