

book_list = [(1, 'java', 1000, 820, 'resd', 'magazine')]
user_list = [(1, "helly", "satellite", "helly@mail.com", 912345)]
issue_book_list = []
avail_list = [(1, 'java', 1000, 820, 'red', 'magazine')]

class Library:

    def add_book(self, detail):
        book_list.append(detail)
        avail_list.append(detail)

        return book_list, avail_list

    def issue_book(self, bookname):
        for book in issue_book_list:
            if(book[1] == bookname):
                return print(" book is already been issued")
            elif book[1] != bookname:
                return print("book does not exist")

        else:
            for book in book_list:
                if book[1] == bookname:
                    issue_book_list.append(book)
                    print("Your book is issued.")


            for book in avail_list:
                if book[1] == bookname:
                    avail_list.remove(book)
                    print
                    return issue_book_list, avail_list, book_list


    def return_book(self, b_name):
        for book in issue_book_list:
            if(book[1] == b_name):
                issue_book_list.remove(book)
                avail_list.append(book)
                print("your book has been returned")
        return issue_book_list, avail_list

    def availble_book(self):
        print(avail_list)

    def display_book(self):
        print(book_list)

    def statistics(self):
        print("Number of Total Books in Library: ", len(book_list))
        print("Number of total issue Books: ", len(issue_book_list))
        print("Number of Available Books: ", len(avail_list))





