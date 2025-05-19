class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} the Dog {self.breed}  says Woof!")

dog1 = Dog("Buddy", "Golden Retriever") 
dog1.bark() 
dog2 = Dog("Max", "Bulldog") 
dog2.bark()         