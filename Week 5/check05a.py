"""
File: check05a.py

To this file you need to add:

A Ship class with member variables: x, y, dx, dy
It should have two simple method: advance and draw

Then to the provided Game class, add calls to your draw
and advance.

You should not need to modify the main function.
"""

import random


# TODO: Define your Ship class here
''' Create a Ship class '''
class Ship:
    ''' Create an __init__ method that sets x, y, dx, and dy to 0. '''
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
    
    ''' Create a draw method that prints the text, "Drawing ship at (x, y)". '''
    def draw(self):
        print("Drawing ship at ({}, {})".format(self.x, self.y))
        
    ''' Create an advance method that adds dx to x, and dy to y. '''
    def advance(self):
        self.x += self.dx
        self.y += self.dy

class Game:
    def __init__(self, dx, dy):
        self.ship = Ship()

        # Set the ship's initial velocity
        self.ship.dx = dx
        self.ship.dy = dy

    def on_draw(self):
        #TODO: Add a call to the draw method of self.ship
        ''' In the Game class on_draw method, call your ship's draw method. '''
        self.ship.draw()

    def update(self):
        #TODO: Add a call to the advance method of self.ship
        ''' In the Game class update method, call your ship's advance method. '''
        self.ship.advance()


def main():
    """
    The main function sets up the game class and calls its
    methods repeatedly, just like will happen in actual games.
    
    You should not need to change anything here:
    """

    seed = input("Enter a random seed: ")
    random.seed(seed)

    dx = random.randint(-4, 4)
    dy = random.randint(-4, 4)

    print("Starting the ship with velocity ({}, {})".format(dx, dy))

    game = Game(dx, dy)

    for i in range(20):
        game.update()
        game.on_draw()

if __name__ == "__main__":
    main()
