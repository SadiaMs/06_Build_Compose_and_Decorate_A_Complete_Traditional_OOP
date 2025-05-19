class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting price")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print("Setting price to", value)
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price

# Create a product
product = Product(100)
print(product.price)

# Update the price
product.price = 150

# Try to set a negative price
try:
    product.price = -50
except ValueError as e:
    print(e)

# Delete the price
del product.price

# Try to access the price after deletion
try:
    print(product.price)
except AttributeError:
    print("Price attribute has been deleted")