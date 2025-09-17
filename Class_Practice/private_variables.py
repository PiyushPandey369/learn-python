'''

    Private Variables

    Create a class BankAccount with a private variable __balance.

    Write methods to deposit, withdraw, and show balance.

    Try accessing __balance directly from outside the class.

    Concept: How Python implements encapsulation and name mangling.

'''
class BankAccount:
    def __init__(self):
        self.__balance=1000
        self.deposit()
    
    def deposit(self):
        print(self.__balance)
        
b=BankAccount() #o/p: 1000
b.__balance=50
b.deposit() #o/p: 1000
b._BankAccount__balance = 1563
b.deposit() #o/p: 1563