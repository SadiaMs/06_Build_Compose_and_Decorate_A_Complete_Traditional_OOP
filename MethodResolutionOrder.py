class A:
    def show(self):
        print("In class A")

class B(A):
    def show(self):
        print("In class B")

class C(A):
    def show(self):
        print("In class C")

class D(B, C):
    pass
d = D()
d.show()  # This will call the show method from class B due to the method resolution order (MRO)
print(D.mro())  # This will show the method resolution order for class D
