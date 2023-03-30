def searcher():
    import time
    #some 4 secocnd time consuming task
    book = "This is a book on pradeep and codewithpradeep"
    time.sleep(5)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")

        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("pradeep")

search.close()