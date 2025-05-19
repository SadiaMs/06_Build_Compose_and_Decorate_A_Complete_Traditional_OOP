class Car:
    brand = ""
    def start(self):
        print(f"{self.brand} car is starting...")
my_car = Car()
my_car.brand = "BMW"
my_car.start()  # Output: BMW car is starting.        
       