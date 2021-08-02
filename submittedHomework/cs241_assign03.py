'''
File: nyAssign03.py

Assignment: Write a Python 3 program to model driving a robot around in an environment.

Credit: Some of the code were copied from https://www.youtube.com/watch?v=K5RuaZuB0V4&t=4s

'''
# Create the Robot Class and Assign Member Variables
class Robot:
    def __init__(self, xCordinate, yCordinate, fuelAmount):
        self.x_cordinate = xCordinate
        self.y_cordinate = yCordinate
        self.fuel_amount = fuelAmount
    
    # Member object to display check and handle fuel status and quantity 
    def fuel_message(self):
        if(self.fuel_amount <= 0):
            flag = True
            print("Insufficient fuel to perform action")
            return flag
        else:
            self.fuel_amount -= 5
        return
    
    # Member function for left robot movement   
    def move_left(self):
        flag = self.fuel_message()
        if not flag:
            self.x_cordinate -= 1
        return
    
    # Member function for right robot movement 
    def move_right(self):
        flag = self.fuel_message()
        if not flag:
            self.x_cordinate += 1
        return
    
    # Member function for upward robot movement 
    def move_up(self):
        flag = self.fuel_message()
        if not flag:
            self.y_cordinate -= 1
        return
    
    # Member function for downward robot movement 
    def move_down(self):
        flag = self.fuel_message()
        if not flag:
            self.y_cordinate += 1
        return
    
    # Member function for lfiring laser and handling of fuel 
    def fire_laser(self):
        if(self.fuel_amount < 15):
            print("Insufficient fuel to perform action")
        else:
            print("Pew! Pew!")
            self.fuel_amount -= 15
        return
    
    # Member function for displaying of cordinates and fuel status 
    def display_status(self):
        print("({0}, {1}) - Fuel: {2}".format(self.x_cordinate, self.y_cordinate, self.fuel_amount))
        return 
        
    # Member function for controlling robot 
    def prompt_command(self):
        action = ""
        while (action != "quit"):
            action = input("Enter command: ")
            if (action == "left"):
                self.move_left()
            elif (action == "right"):
                self.move_right()
            elif (action == "up"):
                self.move_up()
            elif (action == "down"):
                self.move_down()
            elif (action == "fire"):
                self.fire_laser()
            elif (action == "status"):
                self.display_status()
            elif (action == "quit"):
                print("Goodbye.")
                exit()

# Non-member function for initializing and calling an robot object 
def main():
    callRobot = Robot(10, 10, 100);
    callRobot.prompt_command()

if __name__ == "__main__":
    main()
            