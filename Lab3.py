class Book:
    def __init__(self):
        self.bookID = ""
        self.title = ""
        self.authorID = None
        self.publisher = ""
        self.yearOfPublication = ""
    def add_Book(self):
        self.bookID = input("Enter the book ID (based on order of creation, 0 to start): ")
        self.title = input("Enter the book title: ")
        self.publisher = input("Enter the book publisher: ")
        self.yearOfPublication = input("Enter the year of publication: ")
    def edit_Book(self):
        while True:
            option = input("Choose One of the following:\n"
                           "1. Edit book ID:\n"
                           "2. Edit the book title:\n"
                           "3. Edit the publisher:\n"
                           "4. Edit the publication year:\n"
                           "5. exit the 'edit_Book' program")
            if option == '1':
                self.bookID = input("Input book ID (based on order of creation, 0 to start): ")
            elif option == '2':
                self.title = input("Enter the book title: ")
            elif option == '3':
                self.publisher = input("Enter the book publisher: ")
            elif option == '4':
                self.yearOfPublication = input("Enter the publication year: ")
            elif option == '5':
                break
            else:
                print("Error: Invalid Input")
    def assign_Author(self, author):
        self.authorID = author
    def display_Book(self):
        print("Book Id: ", self.bookID)
        print("Title: ", self.title)
        print("Author: ", self.authorID)
        print("Publisher: ", self.publisher)
        print("Publication year: ", self.yearOfPublication)

class User:
    def __init__(self):
        self.userID = ""
        self.userName = ""
        self.password = ""
        self.address = ""
        self.phone = ""
        self.emailID = ""
        self.booksBorrowed = []
    def add_User(self):
        self.userID = input("Input User ID (based on order of creation, 0 to start): ")
        self.userName = input("Input User Name: ")
        self.password = input("Input the password: ")
        self.address = input("Input the address: ")
        self.phone = input("Input the phone number: ")
        self.emailID = input("Input the emailID: ")
    def edit_User(self):
        while True:
            option = input("Choose One of the following:\n"
                           "1. Edit User ID:\n"
                           "2. Edit User Name:\n"
                           "3. Edit the password:\n"
                           "4. edit the address:\n"
                           "5. edit the phone number:\n"
                           "6. edit the emailID:\n"
                           "7. exit the 'edit_User' program: ")
            if option == '1':
                self.userID = input("Input User ID: ")
            elif option == '2':
                self.userName = input("Input User Name: ")
            elif option == '3':
                self.password = input("Input the password: ")
            elif option == '4':
                self.address = input("Input the address: ")
            elif option == '5':
                self.phone = input("Input the phone number: ")
            elif option == '6':
                self.emailID = input("Input the emailID: ")
            elif option == '7':
                break
            else:
                print("Error: Invalid Input")
    def borrow_Book(self, book):
        self.booksBorrowed.append(book)
    def display_User(self):
        print("User Id: ", self.userID)
        print("Username: ", self.userName)
        print("Books Borrowed: ")
        for x in self.booksBorrowed:
            print(x.bookID, x.title, x.authorID)

class Author:
    def __init__(self):
        self.authorID = ""
        self.authorName = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.emailID = ""
    def add_Author(self):
        self.authorID = input("Enter the Author ID (based on order of creation, 0 to start): ")
        self.authorName = input("Enter the author's name: ")
        self.affiliation = input("Enter the author's affiliation: ")
        self.country = input("Enter the author's country of origin: ")
        self.phone = input("Enter the author's phone number: ")
        self.emailID = input("Enter the author's email ID: ")
    def edit_Author(self):
        while True:
            option = input("Choose One of the following:\n"
                           "1. Edit Author ID:\n"
                           "2. Edit Author Name Name:\n"
                           "3. Edit the author's affiliation:\n"
                           "4. edit the author's country origin:\n"
                           "5. edit the phone number:\n"
                           "6. edit the emailID:\n"
                           "7. exit the 'edit_User' program: ")
            if option == '1':
                self.authorID = input("Enter the Author ID (based on order of creation, 0 to start): ")
            elif option == '2':
                self.authorName = input("Enter the author's name: ")
            elif option == '3':
                self.affiliation = input("Enter the author's affiliation: ")
            elif option == '4':
                self.country = input("Enter the author's country of origin: ")
            elif option == '5':
                self.phone = input("Enter the author's phone number: ")
            elif option == '6':
                self.emailID = input("Enter the author's email ID: ")
            elif option == '7':
                break
            else:
                print("Error: Invalid Input")
    def display_Author(self):
        print(self.authorID)
        print(self.authorName)
        print(self.affiliation)
        print(self.country)
        print(self.phone)
        print(self.emailID)

library = []
author_list = []
user_list = []


u = 0
a = 0
b = 0

while True:
    option = input("Choose one of the following:\n"
                    "1. Add a User object\n"
                   "2. Add an author object\n"
                   "3. Add a book object\n"
                   "4. Have a user borrow a book:\n"
                   "5. Display a book:\n"
                   "6. Display a user:\n"
                   "7. Display an Author:\n"
                   "8. Exit the Program: ")
    if option == '1':
        user_list.append(User())
        user_list[u].add_User()
        u += 1
    elif option == '2':
        author_list.append(Author())
        author_list[a].add_Author()
        a += 1
    elif option == '3':
        if len(author_list) == 0:
            print("Unable to Perform the requested task, please ensure there are authors created.")
        else:
            library.append(Book())
            library[b].add_Book()
            book = int(input("Enter the ID of the Book you wish to add an author to: "))
            au = int(input("Enter the ID of the author you wish to assign to the book: "))
            library[book].assign_Author(author_list[au].authorID)
            b += 1
    elif option == '4':
        if len(user_list) == 0 or len(library) == 0:
            print("Unable to Perform the requested task, please ensure there are objects in each list.")
        else:
            us = int(input("Enter the ID of the User that wishes to borrow a book: "))
            bo = int(input("Enter the ID of the book that the User wishes to borrow: "))
            user_list[us].borrow_Book(library[bo])
    elif option == '5':
        if len(library) == 0:
            print("Unable to Perform the requested task, please ensure there are objects in the list.")
        else:
            boo = int(input("Enter the ID of the book you wish to display: "))
            library[boo].display_Book()
    elif option == '6':
        if len(user_list) == 0:
            print("Unable to Perform the requested task, please ensure there are objects in each list.")
        else:
            use = int(input("Enter the ID of the user you wish to display: "))
            user_list[use].display_User()
    elif option == '7':
        if len(author_list) == 0:
            print("Unable to Perform the requested task, please ensure there are objects in each list.")
        else:
            aut = int(input("Enter the ID of the author you wish to display: "))
            author_list[aut].display_Author()
    elif option == '8':
        break
    else:
        print("Error: Invalid Input.")
