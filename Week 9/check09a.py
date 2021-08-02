'''
File: check09a
Purpose: Write programs that correctly use exceptions and error handling to solve problems

author: Sunday Onwuchekwa

'''

class ExceptionHandling:
    def __init__(self):
        self.validNumber = 0
        
    def prompt(self):
        valid_number = False
        while not valid_number:
            try:
                self.validNumber = int(input("Enter a number: "))
                valid_number = True
            except ValueError:
                print("The value entered is not valid")
        return self.validNumber
    
    def display(self):
        print("The result is: {0}".format(self.validNumber * 2))
        
def main():
    handle_error = ExceptionHandling()
    handle_error.prompt()
    handle_error.display()
    
if __name__ == "__main__":
    main()
    