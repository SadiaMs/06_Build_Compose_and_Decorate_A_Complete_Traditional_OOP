class Bank:
    bank_name = "ABC Bank"  # Class variable

    def __init__(self,accountNumber):
        self.accountNumber = accountNumber

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    def showDetails(self):
        print(f"Account Number: {self.accountNumber}, Bank Name: {self.bank_name}")

acco1 = Bank("Sadia")
acco2 = Bank("Mutahir")

Bank.change_bank_name("XYZ Bank")
acco1.showDetails()
acco2.showDetails()


