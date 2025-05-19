class Person:
    def __init__(self,name):
        self.name = name
class Teacher(Person):
    def __init__(self,name,subject):
       super().__init__(name)
       self.subject = subject  

    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")
tea1 = Teacher("Sadia","Maths")
tea1.display()
tea2 = Teacher("Mutahir","English")
tea2.display()