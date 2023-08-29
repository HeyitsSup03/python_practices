class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Available Books:")
        for book in self.books:
            print("-", book)
    def borrowBook(self, name, bookname):
        if bookname in self.books:
            print(f"{name} has borrowed {bookname}.")
            self.books.remove(bookname)
        else:
            print(f"Sorry, {bookname} is currently unavailable for borrowing.")

    def returnBook(self, bookname):
        self.books.append(bookname)
        print(f"{bookname} has been returned.")

    def donateBook(self, bookname):
        self.books.append(bookname)
        print(f"{bookname} has been donated.")
        

class Student:
    def requestBook(self):
        return input("Enter the name of the book you want to borrow: ")

    def returnBook(self):
        name = input("Enter your name: ")
        number = input("Enter your Registration Number: ")
        bookname = input("Enter the name of the book you want to return: ")
        return name,number,bookname

    def donateBook(self):
        return input("Enter the name of the book you want to donate: ")



IIITlibrary = Library(["Upendrakishore Somogro", "Bibhutivushan Somogro", "Chokher Baali"]) 
student = Student() 
while True:
    print("\nMenu:")
    print("1. Display available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Donate a book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        IIITlibrary.displayAvailableBooks()
    elif choice == 2:
        bookname = student.requestBook()
        IIITlibrary.borrowBook("Student", bookname)
    elif choice == 3:
        name,number, bookname = student.returnBook()
        IIITlibrary.returnBook(bookname)
    elif choice == 4:
        bookname = student.donateBook()
        IIITlibrary.donateBook(bookname)
    elif choice == 5:
        print("Thanks for using our library management system!")
        break
    else:
        print("Invalid choice. Please try again.")
