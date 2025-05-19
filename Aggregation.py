class Employee:

  def __init__(self,name,empId):
    self.name = name
    self.empId = empId

  def display(self):
    print( f"Name:{self.name}, ID: {self.empId}" )

class Department:
  def __init__(self,depName,employee):
    self.depName = depName
    self.employee = employee

emp = Employee("Sadia", 101)
dep = Department("HR", emp)
dep.employee.display()

print("\nAccessing Employee details from Department object:")
dep.employee.display()