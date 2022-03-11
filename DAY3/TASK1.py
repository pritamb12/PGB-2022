#program to create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
        
    def seating_capacity(self,capacity):
        return f"The seating capacity for car is {capacity}"
Type=Vehicle(150,60) #object
print("Vehicle with maxspeed {} and mileage {}".format(Type.max_speed,Type.mileage))

#a.Create a Taxi object that will inherit all of the variables and methods of the parent Vehicle class and display it.
class Taxi(Vehicle):
    pass
taxi=Taxi(180,90)
print("Taxi's maxspeed {} and mileage {}".format(taxi.max_speed,taxi.mileage))

#b.Create a Car class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 5
class Car(Vehicle):
    def seating_capacity(self, capacity=5):
        return super().seating_capacity(capacity=5)
car=Car(160,70)
print(car.seating_capacity())
print("Car max speed is {} and mileage is {}".format(car.max_speed,car.mileage))

#c.Define a property that must have the same value for every class instance (object)
class Bus(Vehicle):
    pass
bus=Bus(200,56)
print("Bus maxspeed is {} and mileage is {}".format(bus.max_speed,bus.mileage))