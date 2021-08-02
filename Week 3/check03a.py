# Create a class object: Student
class Student:
    # Constructor
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.id = 0
        
# Function to get student details
def prompt_student():
    Student.FirstName = input("Please enter your first name: ")
    Student.LastName = input("Please enter your last name: ")
    Student.id = int(input("Please enter your id number: "))
    return Student

def display_student(student_detail):
    get_student = student_detail
    print("\nYour information:\n{0} - {1} {2}".format(get_student.id, get_student.FirstName, get_student.LastName))

def main():
    user = prompt_student()
    display_student(user)
    
if __name__ == "__main__":
    main()