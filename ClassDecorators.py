def add_greeting(cls):
    class WrappedClass(cls):
        def greet(self):
            return "Hello from Decorator!"
    return WrappedClass

@add_greeting
class Person:
    def __init__(self,name):
        self.name = name

    def say_name(self):
        return f"My name is {self.name}"

person = Person("Alice")
print(person.say_name())
print(person.greet())  # This will call the greet method from the WrappedClass