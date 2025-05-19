class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create a multiplier object with a factor of 3
multiplier = Multiplier(3)

# Test if the object is callable
print(callable(multiplier))  # Output: True

# Call the object like a function
result = multiplier(5)
print(result)  # Output: 15

# Test with different inputs
print(multiplier(10))  # Output: 30
print(multiplier(2.5))  # Output: 7.5