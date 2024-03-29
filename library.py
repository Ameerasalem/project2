class Book:
    def __init__(self, book_id, title, author, level):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.level = level
        self.available = True
class Member:
    def __init__(self, member_id, name, email, level):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_member(self, member):
        self.members.append(member)
    def add_book(self, book):
        self.books.append(book)
    def display_members(self):
        print("ID\n| Name\n | Email\n | Level\n ")
        print("=" * 80)
        for member in self.members:
            print(f"{member.member_id}\n| {member.name}\n | {member.email}\n| {member.level}")
# Six Choice :
    def display_books(self):
        print("ID\n | Title\n | Author\n | Level\n | Availability")
        print("=" * 80)
        for book in self.books:
            availability = "Available" if book.available else "Not Available"
            print(f"{book.book_id}\n | {book.title}\n| {book.author}\n | {book.level}\n | {availability}")

    def find_memberId(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def find_bookId(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
library = Library()
welcome = "Welcome to the Library System"
section = ''' 
1.Add Member  
2.Edit Member  
3.Show members  
4.Delete Member 
5.Add Book 
6.Show Books 
7.Borrow Book 
8.Return Book 
9.Exit 
'''
while True:
    print(section)
    choice = int(input("- Your Choice : "))
    if choice == 1:
        name1 = input("- member name : ")
        email1 = input("- member email : ")
        while email1.find("@") == -1:
            email1 = input("Invalid input! Please enter the Email again : ")
        level1 = input("- the member level (A/B/C): ")
        while not (
                level1.upper() == "A" or level1.upper() == "B"  or level1.upper() == "C"):
            level1 = input(f"Invalid input! Please enter the Member Level again (A/B/C): ")
        print(" Member added successfully.")
        member_id = len(library.members) + 1
        new_member = Member(member_id, name1, email1, level1)
        library.add_member(new_member)
    elif choice == 2:
        member_id = int(input("- Member ID : "))
        member = library.find_memberId(member_id)
        if member:
            name2 = input("- member new name : ")
            email2 = input("- member new email : ")
            level2 = input("- the member new level (A/B/C) : ")
            while not (
                  level2.upper() == "A"  or level2.upper() == "B"  or level2.upper() == "C"):
                level2 = input(f"Invalid input! Please enter the Member Level again (A/B/C): ")
            print(" Member details Updated successfully.")
            member.name = name2
            member.email = email2
            member.level = level2
        else:
            print("MemberID Not Found!!")
    elif choice == 3:
        library.display_members()
    elif choice == 4:
        member_id_to_delete = int(input("- Member ID to delete : "))
        member_to_delete = None
        for member in library.members:
            if member.member_id == member_id_to_delete:
                member_to_delete = member
                break
        if member_to_delete:
            library.members.remove(member_to_delete)
            new_member_id = 1
            for remaining_member in library.members:
                remaining_member.member_id = new_member_id
                new_member_id += 1
            print("Member deleted successfully.")
        else:
            print("MemberID Not Found!!")
    elif choice == 5:
        title = input("- Book Title : ")
        author = input("-Book Author : ")
        level1 = input("-the book level (A/B/C): ")
        while not (
                 level1.upper() == "A"  or level1.upper() == "B"  or level1.upper() == "C"):
            level1 = input(f"Invalid input! Please enter the Book Level again (A/B/C): ")
        print(" Book added successfully.")
        book_id = len(library.books) + 1
        new_book = Book(book_id, title, author, level1)
        library.add_book(new_book)
    elif choice == 6:
        library.display_books()
    elif choice == 7:
        memberr_id = int(input("-Member ID : "))
        book_id = int(input("-Book ID : "))
        member = library.find_memberId(memberr_id)
        book = library.find_bookId(book_id)
        if member and book:
            if book.available and member.level.upper() == book.level.upper():
                book.available = False
                member.borrowed_books.append(book)
                print(f"#{member.name} has borrowed the book : {book.title} ")
            elif not book.available:
                print("Book is not available to borrowing.")
            else:
                print("Member level is not suitable to borrowing  !!")
        else:
            print("Member or Book not Found !!")
    elif choice == 8:
        member_id = int(input("- Member ID : "))
        book_id = int(input("-Book ID : "))
        member = library.find_memberId(member_id)
        book = library.find_bookId(book_id)
        if member and book:
            for borrowed_book in member.borrowed_books:
                if borrowed_book == book:
                    book.available = True
                    member.borrowed_books.remove(book)
                    print(f"#{member.name} has returned the book : {book.title} ")
                else:
                    print("Not found :(")
        else:
            print("Member or Book not Found !!")
    else:
       print("Invalid choice. Please select a valid option.")