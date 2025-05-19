class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Your name is {self.name}, your marks is {self.marks}")

if __name__ == "__main__":
    s1 = Student("Sadia", 90)
    s1.display()

    s2 = Student("Mutahir", 100)
    s2.display()

    s3 = Student("Moatar", 1000)
    s3.display()

    s4 = Student("Haziq", 1000)
    s4.display()
