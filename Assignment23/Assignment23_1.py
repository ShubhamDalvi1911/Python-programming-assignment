'''Write a Python program to implement a class named BookStore with the following specifications:
   - The class should contain two instance variables:
     - Name (Book Name)
     - Author (Book Author)
   - The class should contain one class variable:
     - NoOfBooks (initialize it to 0)
   - Define a constructor (__init__) that accepts Name and Author and initializes instance variables.
   - Inside the constructor, increment the class variable NoOfBooks by 1 wherever a new object is created.
   - Implement an instance method:
     - Display() - should display book details in the format: <BookName> by <Author>. No of books: <NoOfBooks>'''

class BookStore:
    NoOFBooks = 0
    def __init__(self, Name , Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOFBooks = BookStore.NoOFBooks + 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of Books: {BookStore.NoOFBooks}")

Obj1 = BookStore("Price Action", "Sunil Gujar")
Obj1.Display()

Obj2 = BookStore("Surrounded by idot", "Thomas Ericson")
Obj2.Display()

Obj3 = BookStore("C programming ", "Danis Richi")
Obj3.Display()

Obj4 = BookStore("Python","Gudo Van Raso")
Obj4.Display()
