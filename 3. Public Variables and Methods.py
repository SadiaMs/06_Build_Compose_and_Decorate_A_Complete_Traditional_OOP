class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):        # public method
        print(f"The {self.brand} car is starting...")

# Example usage:
my_car = Car("Toyota")

# Accessing public variable
print("Car Brand:", my_car.brand)

# Calling public method
my_car.start()
