class ATM:
    __count = 1  # Class variable to track number of ATM instances

    def __init__(self):
        self.__pin = ""         # Private PIN
        self.__balance = 0      # Private balance
        self.sno = ATM.__count  # Serial number
        ATM.__count += 1

    # Getter and setter for PIN
    def get_pin(self):
        return self.__pin

    def set_pin(self, pin):
        if isinstance(pin, str):
            self.__pin = pin
        else:
            print("PIN must be a string!")

    # Static methods for instance count
    @staticmethod
    def get_count():
        return ATM.__count

    @staticmethod
    def set_count(count):
        if isinstance(count, int):
            ATM.__count = count
        else:
            print("Count must be an integer!")

    # Create a new PIN
    def create_pin(self):
        self.__pin = input("Enter your PIN: ")
        print("PIN set successfully.")

    # Deposit money
    def deposit_cash(self):
        entered_pin = input("Enter your PIN to proceed: ")
        if entered_pin == self.__pin:
            amount = float(input("Enter amount to deposit: "))
            self.__balance += amount
            print("Amount deposited successfully.")
        else:
            print("Incorrect PIN! Try again later.")

    # Withdraw money
    def withdraw_cash(self):
        entered_pin = input("Enter your PIN to proceed: ")
        if entered_pin == self.__pin:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Incorrect PIN! Try again later.")

    # Check balance
    def check_balance(self):
        entered_pin = input("Enter your PIN to proceed: ")
        if entered_pin == self.__pin:
            print(f"Your current balance is: {self.__balance}")
        else:
            print("Incorrect PIN! Try again later.")

    # Menu-driven operations
    def menu(self):
        print(f"Welcome! Your ATM serial number is {self.sno}")
        while True:
            choice = input('''
Choose an operation:
1) Create PIN
2) Deposit Cash
3) Withdraw Cash
4) Check Balance
5) Exit
Enter your choice: ''')

            if choice == "1":
                self.create_pin()
            elif choice == "2":
                self.deposit_cash()
            elif choice == "3":
                self.withdraw_cash()
            elif choice == "4":
                self.check_balance()
            elif choice == "5":
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


# Example usage
if __name__ == "__main__":
    atm1 = ATM()
    atm1.menu()  # Menu runs only when explicitly called

    atm2 = ATM()
    print(f"Second ATM serial number: {atm2.sno}")

    atm3 = ATM()
    print(f"Third ATM serial number: {atm3.sno}")

    print(f"Total ATMs created: {ATM.get_count() - 1}")  # Minus 1 because __count starts at 1
