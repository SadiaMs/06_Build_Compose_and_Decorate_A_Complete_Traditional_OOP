class Student:
    def __init__(self, name, marks):
        self.name = name      # using self to refer to the instance attribute
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Example usage:
student1 = Student("Ali", 85)
student1.display()
