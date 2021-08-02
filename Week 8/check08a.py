'''
File: check08a.py
Purpose: practice getter and setter functions

@author: Sunday Onwuchekwa
'''

'''
    Create a class to hold a student's GPA. This GPA should be in the range of 0.0 to 4.0.
    Your class should only store the numeric gpa value, NOT a letter
'''
class GPA:
    ''' Create an __init__() function to set the initial value to 0.0. '''    
    def __init__(self):
        self.gpa = 0.0
    
    ''' Create a function for get_gpa() and set_gpa(value) that get
        and set the GPA stored in this class
    '''
    def get_gpa(self):
        return self.gpa
    
    def set_gpa(self, gpa):
        ''' If a GPA less that 0 is entered, you should not set the
            internal value to that, but instead, set it to 0. Similarly,
            if a value greater than 4 is entered, you should instead set
            the value to 4.0.
        '''
        if gpa < 0:
            self.gpa = 0.0
        elif gpa > 4:
            self.gpa = 4.0
        else:
            self.gpa = gpa
    
    '''
        You should also create a function for get_letter() and
        set_letter(letter). But you should NOT store the letter
        internally
    '''
    def get_letter(self):
        '''
            When someone calls the get_letter() function, you should
            determine the correct letter for the stored gpa, and return it
        '''
        if self.gpa < 1:
            return "F"
        elif self.gpa < 2:
            return "D"
        elif self.gpa < 3:
            return "C"
        elif self.gpa < 4:
            return "B"
        else:
            return "A"
    
    def set_letter(self, letters):
        letter = letters.upper();
        '''
            when the set_letter() function is called, you should
            determine the appropriate gpa value and store that
        '''
        if letter == "F":
            self.gpa = 0
        elif letter == "D":
            self.gpa = 1
        elif letter == "C":
            self.gpa = 2
        elif letter == "B":
            self.gpa = 3
        else:
            self.gpa = 4

def main():
    student = GPA()

    print("Initial values:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    value = float(input("Enter a new GPA: "))

    student.set_gpa(value)

    print("After setting value:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

    letter = input("Enter a new letter: ")

    student.set_letter(letter)

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.get_gpa()))
    print("Letter: {}".format(student.get_letter()))

if __name__ == "__main__":
    main() 