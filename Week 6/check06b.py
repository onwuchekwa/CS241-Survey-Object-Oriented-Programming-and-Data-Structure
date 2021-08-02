'''
File: check06b
Purpose: Write programs that correctly use inheritance to solve problems
@author: Sunday Onwuchekwa
'''

''' The Phone class prompt for and display phone numbers '''
class Phone:
    def __init__(self):
        ''' Three integers for the different parts of a phone number '''
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0
        
    def prompt_number(self):
        ''' This ask the user to enter each element of a phone number ''' 
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))
    
    def display(self):
        print("Phone info:")
        ''' This display the number in the format "(areaCode)prefix-suffix" '''
        print("({}){}-{}".format(self.area_code, self.prefix, self.suffix))

''' SmartPhone class extend the Phone class and contain an email address '''
class SmartPhone(Phone):
    def __init__(self):
        super().__init__()
        self.email = ""
    ''' This call the prompt_number method defined in the base class and then additionally prompt for an email address '''    
    def prompt(self):        
        super().prompt_number()
        self.email = input("Email: ")
    
    ''' call the display method defined in the base class and then display the email address '''
    def display(self):
        super().display()
        print("{}".format(self.email))

def main():
    ''' Create the Phone object '''
    phone = Phone()    
    print("Phone:")    
    ''' Call Phone's prompt_number  '''
    phone.prompt_number()
    print()
    ''' Call Phone's display  '''
    phone.display()
    print()
    ''' Create SmartPhone object '''
    smart_phone = SmartPhone()
    print("Smart phone:")
    ''' Call SmartPhone's prompt  '''
    smart_phone.prompt()
    print()
    ''' Call SmartPhone's display  '''
    smart_phone.display()

if __name__ == "__main__":
    main()