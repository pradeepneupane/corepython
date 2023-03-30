class Library:
    def __init__(self,list,name='library'):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"we have to following book in your library{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender book database has been updated.you can take the book now")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self,book):
        self.booklist.append(book)
        print("Book has been updated list")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    pradeep = Library(['python','Rich Dad and poor Dad','Think and grow Rich'],"pradeep's library")

    while(True):
        print(f"welcome to the {pradeep.name} library.Enter your your choice to continue")
        print("1.Display Books")
        print("2.Lend a Book")
        print("3.Add a book")
        print("4.Return a Book")

        user_choice = input()

        if user_choice not in ['1','2','3','4']:
            print("please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice==1:
            pradeep.displayBooks()

        elif user_choice==2:
            user = input("Enter your name")
            book = input("Enter the name  of the book you want to lend")
            pradeep.lendBook(user,book)

        elif user_choice==3:
            book = input("Enter your name of book you want to add")
            pradeep.addBook(book)

        elif user_choice==4:
            book = input("Enter the name of the book you want to return")
            pradeep.returnBook(book)

        else:
            print("Not a valid option")

        print("press q to quit and c to continue")

        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue




