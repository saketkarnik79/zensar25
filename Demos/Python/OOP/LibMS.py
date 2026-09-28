class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def issue_book(self):
        if self.is_available:
            self.is_available = False
            print(self.title, "has been issued.")
        else:
            print(self.title, "is already issued.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(self.title, "has been returned.")
        else:
            print(self.title, "is already available.")

    def display_details(self):
        print("\nBook ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)

        if self.is_available:
            print("Status  : Available")
        else:
            print("Status  : Issued")


# Creating a Book object
book1 = Book(1, "Python Programming", "John Smith")

book1.display_details()

# Issue book
book1.issue_book()
book1.display_details()

# Return book
book1.return_book()
book1.display_details()