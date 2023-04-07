
from books import *
from library import *
from user import *


def user_detail():
    print("Enter the user Details")
    user_id = user_list[-1][0] + 1
    print("Your user_id is:", user_id)
    user_name = (input("Enter name:"))
    user_add = (input("Enter address:"))
    user_email = (input("Enter Email:"))
    user_number = (input("mobile no:"))
    return user_id, user_name, user_add, user_email, user_number


def book_detail():
    print("Enter the details of a book")
    if len(book_list) == 0:
        book_id = 1

        book_name = (input("Enter Book name"))
        book_price = (input("Enter a price of book"))
        book_pages = (input("Enter a pages of book"))
        book_author = (input("Enter the Author name"))
        book_type = (input("Enter the type of book"))

    else:
        book_id = book_list[-1][0] + 1
        book_name = (input("Enter Book name"))
        book_price = (input("Enter a price of book"))
        book_pages = (input("Enter a pages of book"))
        book_author = (input("Enter the Author name"))
        book_type = (input("Enter the type of book"))

    return book_id, book_name, book_price, book_pages, book_author, book_type


if __name__ == '__main__':
    my_library = Library()
    print("library management system")
    while True:
        print()
        print("Enter your choice ")
        print("1.new user 2.existing  User")
        choice = int(input('enter the choice'))

        if choice == 1:
            id, name, add, email, number = user_detail()
            user = User(id, name, add, email, number)
            user.new_user()
            print(user_list)

        elif choice == 2:
            count = 0
            # print()
            id = int(input("Enter your id"))
            for user_id in user_list:
                if (user_id[0] == id):
                    count = 1
                    print(id)
                    break

                if count == 0:
                    # print()
                    print("Not valid user id")
                    continue

        while True:

            print("what do you  want to perform:")
            print("1. Add a book")
            print("2. Issue a book")
            print("3. return a book")
            print("4. Show Available Books")
            print("5. Display all the books")
            print("6. Display Statistics")
            print("7. Exit")
            print()
            choice = int(input("Enter choice: "))

            if choice == 1:
                id, name, price, pages, author, type = book_detail()

                if type == "magazine":
                    month = (input("Enter the month"))
                    creator = (input("Enter the creator"))
                    magazine = Magazine(id, name, price, pages, author, type, month, creator)
                    my_library.add_book(magazine.magazine_detail())
                    print("Your book is added ", book_list)

                elif type == "novel":
                    writer = (input("Enter the creator"))
                    novel = Novel(id, name, price, pages, author, type, writer)
                    my_library.add_book(novel.novel_detail())
                    print("Your book is added", book_list)

                else:
                    book = Book(id, name, price, pages, author, type)
                    my_library.add_book(book.book_detail())
                    print("Book is added to the library", book_list)

            elif choice == 2:
                print()
                book_name = str(input("Enter the name which book you want to issue:"))
                my_library.issue_book(book_name)

            elif choice == 3:
                print()
                book_name = str(input("Enter the name which book you want to return:"))
                my_library.return_book(book_name)

            elif choice == 4:
                my_library.availble_book()

            elif choice == 5:
                my_library.display_book()

            elif choice == 6:
                my_library.statistics()

            elif choice == 7:
                exit()

            else:
                print("enter correct choice")
