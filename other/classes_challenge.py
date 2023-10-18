# Create a Rectangle class with attributes length and width. 
# Add methods to calculate the area and perimeter of the rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(5, 10)
print(rect.area())      
print(rect.perimeter()) 

# Create a BankAccount class with attributes account_number and balance. 
# Add methods to deposit and withdraw money from the account.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


acct = BankAccount("1234")

print(acct.get_balance())
acct.deposit(100)
print(acct.get_balance())
acct.withdraw(50)
print(acct.get_balance())
acct.withdraw(1000)


# Create a Car class with attributes make, model, and year. 
# Add methods to get and set the values of the attributes.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    
car = Car("Ford", "Focus", 2020)

print(car.get_make())
car.set_make("toyota")
car.set_model("pickup")
car.set_year(1995)
print(car.get_make())
print(car.get_model())
print(car.get_year())
print(car)


# Create a Product class with attributes name, price, and quantity. 
# Add methods to calculate the total value of the product (price * quantity) 
# and add or remove items from the product inventory.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
    def add_items(self, quantity):
        self.quantity += quantity

    def remove_items(self, quantity):
        if quantity > self.quantity:
            print("insufficiant quantity")
        else:
            self.quantity -= quantity

    def __str__(self):
        return f"{self.name} {self.price} {self.quantity}"
    
prod = Product("macbook pro", 1000, 5)

print(prod.total_value())
prod.add_items(5)
print(prod.quantity)
prod.remove_items(9)
print(prod.quantity)
prod.remove_items(5)
print(prod)