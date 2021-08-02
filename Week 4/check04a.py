'''
File: check04a.py

Purpose: Write programs that correctly use object composition to solve problems.
'''

'''
Create a class for a Person that contains a name and a birth year.
The author of a book will be a Person object.
'''
class Person:
    '''
    Create an initializer for your Person class to set the
    default name to be "anonymous" and the year to be "unknown".   
    '''
    def __init__(self):
        self.name = "anonymous"
        self.year = "unknown"
     
    '''
    Create a method, display that displays the Person's name
    and birth year in the format "name (b. year)"
    '''
    def display(self):
        print("{0} (b. {1})".format(self.name, self.year))

'''
Create a class for a Book that contains a title, an author (of type Person), and a publisher.
'''
class Book:
    def __init__(self):
        '''
        Create an initializer for your Book class to set the default title to be "untitled",
        the author to be a Person, and the publisher to be "unpublished".
        '''
        self.title = "untitled"
        self.author = Person()
        self.publisher = "unpublished"
    
    '''
    Create a method, display that displays the Book's information as follows
    (don't forget to have the book display method call the author's display method):
    '''
    def display(self):
        print(self.title)
        print("Publisher:")
        print("{}".format(self.publisher))
        print("Author:")
        self.author.display()

#create a main function 
def main():
    #Create a new book
    new_book = Book()
    #Call that book's display function
    new_book.display()
    print()
    '''
    Prompts the user for each of the following: author name and birth year, and the books title and publisher.
    '''
    print("Please enter the following:")
    #Sets these values for the current book and it's author.
    new_book.author.name = input("Name: ")
    new_book.author.year = input("Year: ")
    new_book.title = input("Title: ")
    new_book.publisher = input("Publisher: ")
    print()
    #Calls the book's display function again.
    new_book.display()
    
if __name__ == "__main__":
    main()
            