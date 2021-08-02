"""
File: skeet.py
Original Author: Br. Burton
Designed to be completed by others

This program implements an awesome version of skeet.
"""
import arcade
import math
import random
from abc import ABC, abstractmethod


# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15

'''
Point Class
'''
class Point:
    def __init__(self):
        self.x = 0.00
        self.y = 0.00

'''
Velocity Class
'''
class Velocity:
    def __init__(self):
        self.dx = 0.00
        self.dy = 0.00

''' A base class for flying objects. '''
class FlyingObject(ABC):
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        ''' The horizontal component of the velocity should be between
            1 and 5 pixels/frame '''
        self.velocity.dx = random.uniform(1, 5)
        ''' The vertical component of the velocity should be between -2
            and +5 pixels/frame '''
        self.velocity.dy = random.uniform(-2, 5)
        self.alive = True
    
    ''' Objects flying across the screen. '''
    def advance(self):
        self.center.y += self.velocity.dy
        self.center.x += self.velocity.dx
        
    def is_off_screen(self, screen_width, screen_height):
        ''' Check whether flying object move off the screen or not '''
        if (self.center.x > screen_width or self.center.y > screen_height):
            return True
        else:
            return False
    
    ''' Since there are varied flying objects, this method will
        enable each flying objects to be draw uniquely '''
    @abstractmethod
    def draw(self):
        pass
    
''' A class for a bulletthat inherits FlyingObject class, draws the bullet, and fires it. '''
class Bullet(FlyingObject):
    def __init__(self):
        super().__init__()
        self.radius = BULLET_RADIUS
        
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, BULLET_COLOR)
    
    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED

''' A class for a target that inherits FlyingObject class, draws the pigeons, and assign point for each hit '''
class Target(FlyingObject, ABC):
    def __init__(self):
        super().__init__()
        self.center.y = random.uniform(SCREEN_HEIGHT / 2, SCREEN_HEIGHT)
        self.radius = TARGET_RADIUS
    
    ''' Since there are varied flying objects, this method will
        enable each flying objects to be draw uniquely '''
    @abstractmethod
    def draw(self):
        pass
    
    ''' Since there are varied flying objects, this method will
        enable each flying objects to be hit and scored uniquely '''
    @abstractmethod
    def hit(self):
        pass
        
class StandardTarget(Target):
    def __init__(self):
        super().__init__()
    
    ''' Rendered as a circle with a 20px diameter '''
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, TARGET_COLOR)

    def hit(self):
        ''' Destroyed with one hit. '''
        self.alive = False
        ''' 1 point is awarded for hitting it '''
        return 1
    
class StrongTarget(Target):
    def __init__(self):
        super().__init__()
        ''' To give the user a greater chance to hit the strong target,
            it should move more slowly than the others. In particular,
            its horizontal velocity should be taken from the range: 1
            to 3, and it's vertical velocity from the range -2 to +3 '''
        self.velocity.dx = random.uniform(1, 3)
        self.velocity.dy = random.uniform(-2, 2)
        ''' No of Lives '''
        self.no_of_lives = 3
        
    def draw(self):
        ''' Rendered as a circle with a number inside of it '''
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        arcade.draw_text(repr(self.no_of_lives), text_x, text_y, TARGET_COLOR, font_size=20)
    
    def hit(self):
        self.no_of_lives -= 1
        ''' 1 point is awarded for each of the first two hits. '''
        hit = 1        
        ''' It takes 3 hits to destroy this target '''
        if(self.no_of_lives == 0):
            self.alive = False
            ''' 5 points are awarded for the third hit that destroys the target. '''
            hit = 5
        return hit

class SafeTarget(Target):
    def __init__(self):
        super().__init__()
        self.radius = TARGET_SAFE_RADIUS
        
    def draw(self):
        ''' Rendered as a square. '''
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.radius, self.radius, TARGET_SAFE_COLOR)
    
    def hit(self):
        ''' It is destroyed with a single hit '''
        self.alive = False
        ''' A penalty of 10 points is incurred if this target is hit '''
        return -10

class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0
        
        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    It assumes the following classes exist:
        Rifle
        Target (and it's sub-classes)
        Point
        Velocity
        Bullet

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class, but mostly
    you shouldn't have to. There are a few sections that you
    must add code to.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        # TODO: Create a list for your targets (similar to the above bullets)
        self.targets = []

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        # TODO: iterate through your targets and draw them...
        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_collisions()
        self.check_off_screen()

        # decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()

        # TODO: Iterate through your targets and tell them to advance
        for target in self.targets:
            target.advance()

    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        :return:
        """

        # TODO: Decide what type of target to create and append it to the list
        random_number = random.randint(1, 3)
        
        if random_number == 1:
            target = StandardTarget()
            
        if random_number == 2:
            target = StrongTarget()
        
        if random_number == 3:
            target = SafeTarget()            
        
        self.targets.append(target)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your targets list "targets"

        for bullet in self.bullets:
            for target in self.targets:

                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        # its a hit!
                        bullet.alive = False
                        self.score += target.hit()

                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it
        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        :return:
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        :return:
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        # set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        # Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.

        Note: This could be a static method, but we haven't
        discussed them yet...
        """
        # get the angle in radians
        angle_radians = math.atan2(y, x)

        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees

# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()