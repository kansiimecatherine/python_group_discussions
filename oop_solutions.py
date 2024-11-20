#OOP

          #BASICS

class Car:
    def __init__(self, brand, color): # Initializing the class.
        self.brand = brand
        self.color = color

# creating an object of the class car
my_car = Car(brand="Honda", color="Black")

#printing attributes
print(f"\nThe Car Brand is : {my_car.brand}")
print(f"The Car Color is : {my_car.color}",'\n\n')


              #INTERMEDIATE
class Car:
    def __init__(self, brand, color): #Initializing the car object 
        self.brand = brand
        self.color = color
    
    # Method to start the engine
    def start_engine(self):
        print(f"The engine of the {self.color} {self.brand} has started.",'\n\n')

# Create an instance of the Car class
my_car = Car(brand="Honda", color="Black")

# Calling the start_engine method
my_car.start_engine()

                       #ADVANCED

class BankAccount:
    # Initialize the BankAccount object with account_number and balance
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    # Method to deposit an amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have deposited shs.{amount: ,}, New balance: shs.{self.balance: ,}")
        else:
            print("Invalid,Please deposit money.")

    # Method to withdraw an amount
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"You have Withdrawn shs.{amount: ,}, New balance: shs.{self.balance: ,}")
            else:
                print("Insufficient balance.")

    # Method to print the account balance
    def print_balance(self):
        print(f"Account Number is : {self.account_number} ----- Balance: shs.{self.balance: ,}")

# Creating an instance of BankAccount
my_account = BankAccount(account_number="123456789ug", balance=8000)

# Perform operations
my_account.print_balance()
my_account.deposit(50000)
my_account.withdraw(3000)
my_account.withdraw(1500)  
my_account.print_balance()


                  #CHALLENGE



