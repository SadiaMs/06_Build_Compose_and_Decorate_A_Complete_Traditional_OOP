class Bank:
    bank_name = "National Bank"  # class variable shared by all instances

    def __init__(self, customer_name):
        self.customer_name = customer_name

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # change the class variable for all instances

    def display(self):
        print(f"Customer: {self.customer_name}, Bank: {Bank.bank_name}")

# Example usage:
cust1 = Bank("sadia")
cust2 = Bank("Mutahir")

# Display initial bank names
cust1.display()
cust2.display()

# Change bank name using class method
Bank.change_bank_name("Global Trust Bank")

# Display after change
cust1.display()
cust2.display()
