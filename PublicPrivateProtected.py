class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn          # Private variable

# Create an object
emp = Employee("Sadia", 50000, "123-45-6789")

# Accessing public variable
print("Name:", emp.name)  # ✅ Accessible

# Accessing protected variable
print("Salary:", emp._salary)  # ⚠️ Accessible, but not recommended (convention says it's protected)

# Accessing private variable
try:
    print("SSN:", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError as e:
    print("Error accessing private variable __ssn:", e)

# Access private variable using name mangling
print("SSN (accessed via name mangling):", emp._Employee__ssn)  # ✅ Possible but not recommended
