def wordcount(book_path):    
    words = book_text(book_path).split()
    wordcount = len(words)
    return wordcount