# Define a custom exception
class InvalidAgeError(Exception):
    def __init__(self, age):
        message = f"Invalid age: {age}. Age must be 18 or above."
        super().__init__(message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print(f"Age {age} is valid.")

# Test the function
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a valid age.")