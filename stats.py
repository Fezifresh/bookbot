def wordcount(book_path):    
    words = book_text(book_path).split()
    num_of_words = len(words)
    return num_of_words

def book_text(book_path):
    book_text = open(book_path)
    text_string = book_text.read()
    return text_string