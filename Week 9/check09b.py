'''
File: check09b
Purpose: Write programs that correctly use exceptions and error handling to solve problems

author: Sunday Onwuchekwa

'''

class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)
        
def get_inverse(number):
    number = float(number)
    
    if number < 0:
        raise NegativeNumberError("Error: The value cannot be negative")
    
    return 1 / number
    
def main():
    number = input("Enter a number: ")
    try:
        inverse = get_inverse(number)
        print("The result is: {}".format (inverse))
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError as e:
        print(e)
        
if __name__ == "__main__":
    main()
        