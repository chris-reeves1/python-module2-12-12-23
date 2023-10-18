#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

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
    

2. Create a BankAccount class with attributes account_number and balance. 
Add methods to deposit and withdraw money from the account. 

3. Create a Car class with attributes make, model, and year. 
Add methods to get and set the values of the attributes. 

4. Create a Product class with attributes name, price, and quantity. 
Add methods to calculate the total value of the product (price * quantity) 
and add or remove items from the product inventory. 

Harder challenge (stretch goal): 

Create a Book class and BookShelf class that can be used to manage a collection of books. 
Create a Book class that has the following attributes: 
title (str), author (str), publisher (str), publication year (int). 
The class should also have a str method that returns the book's information in a 
formatted string. 
Create a BookShelf class that has the following attributes: 
capacity (int), list of books (list). 
The class should have the following methods: 
- add_book: adds a book to the list of books if the shelf is not full 
- remove_book: removes a book from the list of books if it exists on the shelf 
- find_book_by_title: searches for a book by its title 
and returns the book object if found 
- find_books_by_author: searches for books by a specific author 
and returns a list of book objects if found 
The class should also have a str method that returns a string representation 
of the books on the shelf. 

Create four Book objects and add them to a BookShelf object with a capacity of three. 
Test the BookShelf object by adding, removing, and finding books by title and author.
Print the BookShelf object after each action.

Alternative stretch goal: rewrite the rock/paper/scissor app using a class. 
