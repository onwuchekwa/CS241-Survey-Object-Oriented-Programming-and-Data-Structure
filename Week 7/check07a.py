"""
File: check07a.py

Starting template for your checkpoint assignment.
"""

# TODO: Create a base car class here
class Car:
    ''' In the init funtion, set the name variable to be "Unknown model" '''
    def __init__(self, name="Unknown Model"):
        self.name = name
    
    ''' Fill in a default get_door_specs() method that returns
        the string "Unknown doors" '''
    def get_door_specs(self):
        return "Unknown doors"

# TODO: Create a civic class here
''' create a class Civic that inherits from the Car class '''
class Civic(Car):
    def __init__(self):
        Car.__init__(self, name="Civic")
    
    ''' Create a method that overrides the get_door_specs() to return
        the string "4 Doors". '''
    def get_door_specs(self):
        return "4 doors"

# TODO: Create an odyssey class here
class Odyssey(Car):
    def __init__(self):
        Car.__init__(self, name="Odyssey")
    
    ''' Create a method that overrides the get_door_specs() to return
        the string "2 front doors, 2 sliding doors, 1 tail gate". '''
    def get_door_specs(self):
        return "2 front doors, 2 sliding doors, 1 tail gate"

# TODO: Create a Ferrari class here
class Ferrari(Car):
    def __init__(self):
        Car.__init__(self, name="Ferrari")
    
    def get_door_specs(self):
        return "2 butterfly doors"

# TODO: Create your attach_doors function here
# It should accept any type of car and use its
# name and get_door_specs function to print out
# the necessary data.
# It should not be a member function of any class,
# but rather just a "regular" function.
def attach_doors(car_type):
    car = car_type
    print("Attaching doors to {} - {}".format(car.name, car.get_door_specs()))


def main():
    car1 = Civic()
    car2 = Odyssey()
    car3 = Ferrari()

    attach_doors(car1)
    attach_doors(car2)
    attach_doors(car3)

if __name__ == "__main__":
    main()
