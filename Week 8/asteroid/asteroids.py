"""
File: asteroids.py
Original Author: Br. Burton
Designed to be completed by others

This program implements the asteroids game.
"""
import arcade
import math
import random
from abc import ABC, abstractmethod

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

class Point:
    ''' Set the x and y coordinates at the center '''
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        
class Velocity:
    ''' Set the speed and movement of the objects '''
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0

class LifeBar:
    ''' Create the life bar of the ship '''
    def __init__(self):
        self.center = Point()
        self.center.x = 60
        self.center.y = SCREEN_HEIGHT - 20
        self.alive = True
        self._width = 100
        self.height = 20
        self.color = arcade.color.GREEN
        
    @property
    def width(self):
       pass
    
    def draw(self):
        pass
    
    def life_lost(self):
        pass

class FlyingObject(ABC):
    ''' Create a common interface for ship, bullet, and asteroid '''
    def __init__(self, img):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.radius = SHIP_RADIUS       
        self.img = img
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.angle = 0
        self.speed = 0
        self.direction = 0
        self.alpha = 255
    
    def draw(self):
        ''' Draw all types of Flying Objects '''
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, self.alpha)
    
    def advance(self):
        ''' Movement of the Flying Objects '''
        self.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    def wrap(self, screen_width, screen_height):
        ''' if an object goes off the right edge of the
            screen, it should appear on the left edge '''
        if self.center.x > screen_width:
            self.center.x -= screen_width
        if self.center.x < 0:
            self.center.x += screen_width
        if self.center.y > screen_height:
            self.center.y -= screen_height
        if self.center.y < 0:
            self.center.y += screen_height
    
class Bullet(FlyingObject):
    ''' Create a bullet that is a flying object '''
    def __init__(self):
        super().__init__("images/laserBlue01.png")
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.speed = BULLET_SPEED

    ''' when bullet is fired, it follows the angle and velocity of the
        ship. '''
    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle + 90)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle + 90)) * BULLET_SPEED
        return (self.velocity.dx, self.velocity.dy)
    
    ''' The bullets are stored at the point of ship and follows the
        speed and angle of the ship '''
    def bullet_storage(self, ship):
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.angle = ship.angle - 90
        self.velocity.dx = ship.velocity.dx + self.fire(ship.angle)[0]
        self.velocity.dy = ship.velocity.dy + self.fire(ship.angle)[1]    
    
class Ship(FlyingObject):
    ''' Create a ship that is a flying object '''
    def __init__(self):
        super().__init__("images/playerShip1_orange.png")
        self.radius = SHIP_RADIUS
        self.center.x = SCREEN_WIDTH // 2
        self.center.y = SCREEN_HEIGHT // 2
        self.turn = SHIP_TURN_AMOUNT
        
class Asteroid(FlyingObject, ABC):
    ''' Create a common interface for all astroid type '''
    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0
        self.speedspin = 0
    
    def advance(self):
        self.angle += self.speedspin
        super().advance()
    
    @abstractmethod    
    def divide(self):
        pass
    
    def hit(self):
        pass
    
class SmallAsteroid(Asteroid):
    ''' Small Asteroids that is an asteroid'''
    def __init__(self):
        super().__init__("images/meteorGrey_small1.png")
        self.radius = SMALL_ROCK_RADIUS
        self.spinspeed = SMALL_ROCK_SPIN
        self.speed = BIG_ROCK_SPEED + 5
    
    def divide(self):
        pass

class MediumAsteroid(Asteroid):
    ''' Middle Asteroids that is an asteroid'''
    def __init__(self):
        super().__init__("images/meteorGrey_med1.png")
        self.radius = MEDIUM_ROCK_RADIUS
        self.speedspin = MEDIUM_ROCK_SPIN
        self.speed = BIG_ROCK_SPEED + 2
    
    def divide(self):
        pass
        
class LargeAsteroid(Asteroid):
    ''' Large Asteroids that is an asteroid'''
    def __init__(self):
        super().__init__("images/meteorGrey_big1.png")
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.radius = BIG_ROCK_RADIUS
        self.speedspin = BIG_ROCK_SPIN
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def divide(self):
        pass

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        self.held_keys = set()

        # TODO: declare anything here you need the game class to track
        self.ship = Ship()
        
        self.asteroids = []
        self.bullets = []        
        
        for i in range(INITIAL_ROCK_COUNT):
            bigRock = LargeAsteroid()
            self.asteroids.append(bigRock)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object
        for asteroid in self.asteroids:
            asteroid.draw()
        
        for bullet in self.bullets:
            bullet.draw()
        
        self.ship.draw()
  
    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
               
        for asteroid in self.asteroids:
            asteroid.advance()            
            # asteroid.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
            
        for bullet in self.bullets:
            bullet.advance()
        
        self.ship.advance()        
        # self.ship.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)
        
    # TODO: Check for collisions
    """
    Checks to see if bullets have hit targets.
    Updates scores and removes dead items.
    :return:
    """

    # NOTE: This assumes you named your asteroids list "asteroids"
    def check_collisions(self):
        
        ''' Removes any dead objects from the list. '''
        self.cleanup_zombies()
        
    def cleanup_zombies(self):
        """
        Removes any dead bullets from the list.
        :return:
        """
        for bullet in self.bullets:
            if (abs(self.ship.center.x - bullet.center.x) > BULLET_LIFE or abs(self.ship.center.y - bullet.center.y) > BULLET_LIFE):
                bullet.alive = False
            if not bullet.alive:
                self.bullets.remove(bullet)
       
    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle += self.ship.turn

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle -= self.ship.turn

        if arcade.key.UP in self.held_keys:
            self.ship.velocity.dx -= math.cos(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy += math.sin(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT

        if arcade.key.DOWN in self.held_keys:
            self.ship.velocity.dx += math.cos(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT
            self.ship.velocity.dy -= math.sin(math.radians(self.ship.angle + 90)) * SHIP_THRUST_AMOUNT

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                bullet = Bullet()
                bullet.bullet_storage(self.ship)
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()