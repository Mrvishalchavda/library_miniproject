class Library:
    def __init__(self, list1, name):
        self.name = name
        self.list = list1
        self.issued_book = {}

    def display_book(self):
        for book in self.list:
            for i in book:
                print(f"{i} writen by {book[i]}")

    def add_book(self, name, authore):
        self.list.append({name: authore})
        print("you book is added sucesfully")

    def issue_book(self, bookname, use):
        if bookname not in self.issued_book.keys():
            self.issued_book.update({bookname: use})
        else:
            print("book is alredy taken by someone other")

    def return_book(self, book):
        self.issued_book.pop(book)


if __name__ == '__main__':
    lis = [{'c++': 'code'}, {'ritch dad poor dad': 'write'}, {'abc': 'de'}]
    vishal = Library(lis, "first")
    while(True):
        print(f"welcome to {vishal.name}'s library please select your task")
        print("1- display book \n2- add book \n3- issue book\n4-return book")
        user_input = (input())
        while(True):
            if user_input not in ["1", "2", "3", "4"]:
                print("enter valid input")
                user_input = (input())
            else:
                print("Enter valid input")
                break
        if user_input == "1":
            vishal.display_book()
        elif user_input == "2":
            bname = input("please enter your book name witch you want to add\n")
            author = input("enter author name\n")
            vishal.add_book(bname, author)
        elif user_input == "3":
            bname = input("please enter bookname witch you want to Issue\n")
            user = input("enter your name\n")
            vishal.issue_book(bname, user)
        elif user_input == "4":
            bname = input("please enter bookname witch you want to return\n")
            vishal.return_book(bname)
        else:
            print("please enter valid input\n")
        print("enter \"q\" for quite and 'c' for contine\n")
        user_input2 = input()
        if user_input2 == "q":
            quit()
        else:
            continue
