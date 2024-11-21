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
            print(f"You have deposited shs.{amount: ,} and the new balance is : shs.{self.balance: ,}")
        else:
            print("Invalid input,Please deposit money.")

    # Method to withdraw an amount
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
                self.balance -= amount
                print(f"You have Withdrawn shs.{amount: ,}, New balance: shs.{self.balance: ,}")
        else:
            print("Insufficient balance.")

    # Method to print the account balance
    def print_balance(self):
        print(f"Account Number is : {self.account_number} ----- Balance: shs.{self.balance: ,}")

# Creating an instance of BankAccount
account = BankAccount(account_number="123456789ug", balance=8000)

# Perform operations
account.print_balance()
account.deposit(50000)
account.withdraw(3000)
account.withdraw(1500)  
account.print_balance()


                  #CHALLENGE

class Library:
    def __init__(self):
        self.books = []  # Storing books as dictionaries

    def add_book(self, title, author):
        book = {"title": title, "author": author, "available": True}
        self.books.append(book) 
        print(f"\nThe book added is : '{title}' by  {author}.")

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"Book removed: '{title}'.")
                return
        print(f"\nBook not found: '{title}'.")

    def is_book_available(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                return book["available"]
        print(f"\nBook not found: '{title}'.")
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["available"]:
                    book["available"] = False
                    print(f"You borrowed: '{title}'.")
                else:
                    print(f"\n'{title}' is currently unavailable.")
                return
        print(f"Book not found: '{title}'.")

    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if not book["available"]:
                    book["available"] = True
                    print(f"\nThank you for returning: '{title}'.",'\n')
                else:
                    print(f"\n'{title}' was not borrowed.")
                return
        print(f"Book not found: '{title}'.")

    def list_books(self):
        if not self.books:
            print("\nThe library has no books.")
        else:
            print("\nThe books in the library are:")
            for book in self.books:
                status = "Available" if book["available"] else "Unavailable"
                print(f"\n - '{book['title']}' by {book['author']} ({status})")


library = Library()

library.add_book("The Hobbit", "J.R.R. Tolkien")
library.add_book("1984", "George Orwell")
library.list_books()

library.borrow_book("1984")
library.list_books()

library.return_book("1984")
library.list_books()

library.remove_book("The Hobbit")
library.list_books()

