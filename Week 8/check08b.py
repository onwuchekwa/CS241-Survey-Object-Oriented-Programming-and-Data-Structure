'''
File: check08b.py
Purpose: Write programs that correctly use encapsulation and properties to solve problems
'''

'''
Create a class to hold a student's GPA. This GPA should be in the range of 0.0 to 4.0.
Your class should only store the numeric gpa value, NOT a letter
'''
class GPA:
    ''' Change the variable that you stored the GPA value in to begin with an underscore '''
    def __init__(self):
        self._gpa = 0.0
    
    ''' Change your getters and setters to begin with underscores '''
    def _get_gpa(self):
        return self._gpa
    
    def _set_gpa(self, gpa):
        if gpa < 0:
            self._gpa = 0.0
        elif gpa > 4:
            self._gpa = 4.0
        else:
            self._gpa = gpa
            
    ''' Add a property named gpa for the _get_gpa() and _set_gpa(value)
        functions using the syntax: property(_get_gpa, _set_gpa) in your
        class.
    '''
    gpa = property(_get_gpa, _set_gpa)
    
    '''  specify the property using the @property syntax for the getter '''
    @property
    def letter(self):
        if self._gpa < 1:
            return "F"
        elif self._gpa < 2:
            return "D"
        elif self._gpa < 3:
            return "C"
        elif self._gpa < 4:
            return "B"
        else:
            return "A"
    
    '''  specify the property using the @letter.setter syntax for the setter '''
    @letter.setter
    def letter(self, letters):
        letter = letters.upper();
        if letter == "F":
            self._gpa = 0
        elif letter == "D":
            self._gpa = 1
        elif letter == "C":
            self._gpa = 2
        elif letter == "B":
            self._gpa = 3
        else:
            self._gpa = 4

def main():
    student = GPA()
    
    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))
    
    '''  All calls to student.get_gpa() should be replaced
        with student.gpa
    '''
    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    ''' All calls to student.set_gpa(xx) should be replaced with student.gpa = xx '''
    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main() 
