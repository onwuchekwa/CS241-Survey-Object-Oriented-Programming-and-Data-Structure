'''
File: check06a
Purpose: Write programs that correctly use inheritance to solve problems.

@author: Sunday Onwuchekwa
'''
''' Create a Book class as a parent '''
class Book:
    def __init__(self):
        ''' Attributes of a Book '''
        self.title = ""
        self.author = ""
        self.publication_year = 0
    
    ''' Prompt users to supply book details '''
    def prompt_book_info(self):
        self.title = input("Title: ")
        self.author = input("Author: ")
        self.publication_year = int(input("Publication Year: "))
    
    ''' Display book details '''
    def display_book_info(self):
        print("{} ({}) by {}".format(self.title, self.publication_year, self.author))            

''' Subclass TextBook inheriting from Parent, Book '''
class TextBook(Book):
    def __init__(self):
        super().__init__()
        self.subject = ""
        
    ''' Prompt users to supply book subject '''
    def prompt_subject(self):
        super().prompt_book_info()
        self.subject = input("Subject: ")
    
    ''' Display book subject '''
    def display_subject(self):
        super().display_book_info()
        print("Subject: {}".format(self.subject))

''' Subclass PictureBook inheriting from Parent, Book '''
class PictureBook(Book):
    def __init__(self):
        super().__init__()
        self.illustrator = ""
    
    ''' Prompt users to supply book illustrator '''
    def prompt_illustrator(self):
        super().prompt_book_info()
        self.illustrator = input("Illustrator: ")
    
    ''' Display book illustrator '''
    def display_illustrator(self):
        super().display_book_info()
        print("Illustrated by {}".format(self.illustrator))

def main():
    ''' Create Book object and call its member methods '''
    book = Book()
    book.prompt_book_info()
    print()
    book.display_book_info()
    print()
    
    ''' Create TextBook object and call its member methods '''
    textbook = TextBook()
    textbook.prompt_subject()
    print()
    textbook.display_subject()
    print()
    
    ''' Create PictureBook object and call its membermethods '''
    picturebook = PictureBook()
    picturebook.prompt_illustrator()
    print()
    picturebook.display_illustrator()

if __name__ == "__main__":
    main()