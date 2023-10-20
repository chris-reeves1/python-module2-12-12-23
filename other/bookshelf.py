# Books and Bookshelf challenge

class Book:
    def __init__(self, title, author, publisher, pub_year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pub_year = pub_year
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublisher: {self.publisher}\nPublication Year: {self.pub_year}"
        

class BookShelf:
    def __init__(self, capacity):
        self.capacity = capacity
        self.books = []
    
    def add_book(self, book):
        if len(self.books) < self.capacity:
            self.books.append(book)
            print(f"{book.title} has been added to the shelf.")
        else:
            print("The shelf is full.")
    
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book.title} has been removed from the shelf.")
        else:
            print("That book is not on the shelf.")
    
    def find_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book
        print("That book is not on the shelf.")
    
    def find_books_by_author(self, author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        if not books:
            print("No books by that author are on the shelf.")
        else:
            return books
    
    def __str__(self):
        if not self.books:
            return "The shelf is empty."
        else:
            output = "Books on shelf:\n"
            for book in self.books:
                output += str(book) + "\n\n"
            return output

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", 1925)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "J. B. Lippincott & Co.", 1960)
book3 = Book("1984", "George Orwell", "Secker & Warburg", 1949)
book4 = Book("The Catcher in the Rye", "J. D. Salinger", "Little, Brown and Company", 1951)

shelf = BookShelf(3)
print(shelf)

shelf.add_book(book1)
shelf.add_book(book2)
shelf.add_book(book3)
shelf.add_book(book4)
print(shelf)

shelf.remove_book(book3)
print(shelf)

book = shelf.find_book_by_title("The Great Gatsby")
print(book)

books = shelf.find_books_by_author("J. D. Salinger")
if books is not None:
    for book in books:
        print(book)
else:
    print("No books found for that author.")