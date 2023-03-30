def searcher():
    import time
    book = "This is a book written by pradeep neupane"
    time.sleep(10)

    while True:
        text = (yield)
        if text in book:
            print("your text is in the book")

        else:
            print("your text is not in the book")


search = searcher()
print("search starter")
next(search)
print("next method run")
print("Enter a word")
word = input()
search.send(word)

search.close()
