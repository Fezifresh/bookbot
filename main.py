def main():
    book_path = 'books/frankenstein.txt'
    words = book_text(book_path).split()
    wordcount = len(words)
    print(f"{wordcount} words found in document")

def book_text(book_path):
    text = get_book_text(book_path)
    return(text)

def get_book_text(path):
    book_text = open(path)
    return book_text.read()

main()


# Meine Lösung
# text = open('books/frankenstein.txt','r')
# print(text.read())
# text.close()