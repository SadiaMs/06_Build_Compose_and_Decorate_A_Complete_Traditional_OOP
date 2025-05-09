class Counter:
    count = 0  # class variable to keep track of number of objects

    def __init__(self):
        Counter.count += 1  # increment count whenever an object is created

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)

# Example usage:
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()
