def main():
    book_path = 'books/frankenstein.txt'
    number_of_characters = count_characters(book_path)
    number_of_words = wordcount(book_path)
    text = book_text(book_path)

    #Report#

    print(f"This is the report for {book_path}\n")

    print(f"{number_of_words} words found in the document\n")
    
    print("This is a list of the characters and the number of their appereance:")
    for a in number_of_characters:
        print(f"The character {a} appeares {number_of_characters[a]} times")
    
    print("\nend of report")

def count_characters(book_path):
    text = book_text(book_path).lower()
    dict_of_characters = {}

    #Liste aller Kleinbuchstaben#
    import string
    string.ascii_lowercase
    letters = (string.ascii_lowercase)
    ##

    for character in text:
        if character not in dict_of_characters and character in letters:
            dict_of_characters[character] = 1
        elif character in letters:
            dict_of_characters[character] += 1
    return dict_of_characters


def wordcount(book_path):    
    words = book_text(book_path).split()
    wordcount = len(words)
    return wordcount

def book_text(book_path):
    book_text = open(book_path)
    text_string = book_text.read()
    return text_string

main()