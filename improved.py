class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added book '{book.title}' to the library.")

    def remove_book(self, title):
        found_books = []
        # Checks if book exists in library first
        for books in self.books:
          if books.title.lower() == title.lower():
            self.books.remove(books)
            print(f"Removed book '{book.title}' from the library.")
          else:
            print(f"Book '{book.title}' is not found in the library.")

    def display_books(self):
        if self.books:
            print("Library Books:")
            for book in self.books:
                print(f"Title: {book.title}\nAuthor: {book.author}\nPublication Year: {book.publication_year}\n")
        else:
            print("The library has no books at the moment.")
      
    
    def search_by_title(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        if found_books:
            print("Books with matching title:")
            for book in found_books:
                print(f"Title: {book.title}\tAuthor: {book.author}\tYear: {book.publication_year}")
        else:
            print("No books found with the given title.")
    
    def search_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        if found_books:
            print("Books with matching author:")
            for book in found_books:
                print(f"Title: {book.title}\tAuthor: {book.author}\tYear: {book.publication_year}")
        else:
            print("No books found with the given author.")




library = Library()
isTrue = True


while isTrue:
  purpose = int(input("""what do you wish to do: 
  1-> Add a book
  2-> Remove book
  3-> Display Library
  4-> Search a book by title
  5-> Seach a book by author
  6-> End
  Input: """))

  if purpose == 1:
    book_name = input('What is the name of this book?: ')
    book_author = input('Who is author of this book? ')
    book_year = int(input('In what year was is published?: '))
    book = Book(book_name, book_author, book_year)
    library.add_book(book)
    library.display_books()
  elif purpose == 2:
    book_name = input('What is the name of the book you wish to remove?')
    library.remove_book(book_name)
  elif purpose == 3:
    library.display_books()
  elif purpose == 4:
    book_name = input("What is the title of book you're looking for? ")
    library.search_by_title(book_name)
  elif purpose == 5:
    book_author = input("Who is the author of the book you'ree looking for? ")
    library.search_by_author(book_author)
  elif purpose == 6:
    isTrue = False
  