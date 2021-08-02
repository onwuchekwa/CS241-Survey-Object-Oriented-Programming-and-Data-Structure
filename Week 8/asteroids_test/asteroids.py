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
        
class FlyingObject(ABC):
    ''' Create a common interface for all flying objects (ship, asteroids, and bullets) '''
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
        
    def advance(self):
        self.wrap()
        self.center.y += self.velocity.dy
        self.center.x += self.velocity.dx
    
    def is_alive(self):
        return self.alive
    
    def draw(self):
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.width, self.height, self.texture, self.angle, 255)
        
    def wrap(self):
        if self.center.x > SCREEN_WIDTH:
            self.center.x -= SCREEN_WIDTH
        if self.center.x < 0:
            self.center.x += SCREEN_WIDTH
        if self.center.y > SCREEN_HEIGHT:
            self.center.y -= SCREEN_HEIGHT
        if self.center.y < 0:
            self.center.y += SCREEN_HEIGHT

class Bullet(FlyingObject):
    def __init__(self, ship_angle, ship_x, ship_y):
        super().__init__("images/laserBlue01.png")
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.speed = BULLET_SPEED
        self.angle = ship_angle - 90
        self.center.x = ship_x
        self.center.y = ship_y
        
    def fire(self):        
        self.velocity.dx -= math.sin(math.radians(self.angle + 90)) * BULLET_SPEED
        self.velocity.dy += math.cos(math.radians(self.angle + 90)) * BULLET_SPEED
    
    def advance(self):
        super().advance()
        self.life -= 1
        if(self.life <= 0):
            self.alive = False

class Ship(FlyingObject):
    def __init__(self):
        super().__init__("images/playerShip1_orange.png")
        self.angle = 1
        self.center.x = (SCREEN_WIDTH/2)
        self.center.y = (SCREEN_HEIGHT/2)
        self.radius = SHIP_RADIUS
        
    def left(self):
        self.angle += SHIP_TURN_AMOUNT
    
    def right(self):
        self.angle -= SHIP_TURN_AMOUNT
    
    def thrust(self):
        self.velocity.dx -= math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
    
    def neg_thrust(self):
        self.velocity.dx += math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT

class Asteroid(FlyingObject):
    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0

class SmallAsteroid(Asteroid):
    def __init__(self):
        super().__init__("images/meteorGrey_small1.png")
        self.speed = BIG_ROCK_SPEED
        self.radius = SMALL_ROCK_RADIUS
        
    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN
    
    def break_apart(self, asteroids):
         self.alive = False

class MediumAsteroid(Asteroid):
    def __init__(self):
        super().__init__("images/meteorGrey_med1.png")
        self.radius = MEDIUM_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
        
    def advance(self):
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN
        
    def break_apart(self, asteroids):
        small1 = SmallAsteroid()
        small1.center.x = self.center.x
        small1.center.y = self.center.y
        small1.velocity.dy = self.velocity.dy + 1.5
        small1.velocity.dx = self.velocity.dx + 1.5
        
        small2 = SmallAsteroid()
        small2.center.x = self.center.x
        small2.center.y = self.center.y
        small2.velocity.dy = self.velocity.dy - 1.5
        small2.velocity.dx = self.velocity.dx - 1.5
        
        asteroids.append(small1)
        asteroids.append(small2)
        self.alive = False
        
class LargeAsteroid(Asteroid):
    def __init__(self):
        super().__init__("images/meteorGrey_big1.png")
        self.radius = BIG_ROCK_RADIUS
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed

    def advance(self):
        super().advance()
        self.angle += BIG_ROCK_SPIN
        
    def break_apart(self, asteroids):
        med1 = MediumAsteroid()
        med1.center.x = self.center.x
        med1.center.y = self.center.y
        med1.velocity.dy = self.velocity.dy + 2
        
        med2 = MediumAsteroid()
        med2.center.x = self.center.x
        med2.center.y = self.center.y
        med2.velocity.dy = self.velocity.dy - 2
        
        small = SmallAsteroid()
        small.center.x = self.center.x
        small.center.y = self.center.y
        small.velocity.dy = self.velocity.dy + 5
        
        asteroids.append(med1)
        asteroids.append(med2)
        asteroids.append(small)
        self.alive = False

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
        self.asteroids = []
        self.bullets = []
        
        for i in range(INITIAL_ROCK_COUNT):
            bigRock = LargeAsteroid()
            self.asteroids.append(bigRock)
            
        self.ship = Ship()
        

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
        
    def remove_notAliveObjects(self):
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)
        
        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)
                
    def check_collisions(self):
        for bullet in self.bullets:
             for asteroid in self.asteroids:
                 if (bullet.alive and asteroid.alive):
                     distance_x = abs(asteroid.center.x - bullet.center.x)
                     distance_y = abs(asteroid.center.y - bullet.center.y)
                     max_dist = asteroid.radius + bullet.radius
                     if (distance_x < max_dist) and (distance_y < max_dist):
                         asteroid.break_apart(self.asteroids)
                         bullet.alive = False
                         asteroid.alive = False
                         
        for asteroid in self.asteroids:
            if (self.ship.alive and asteroid.alive):
                distance_x = abs(asteroid.center.x - self.ship.center.x)
                distance_y = abs(asteroid.center.y - self.ship.center.y)
                max_dist = asteroid.radius + self.ship.radius
                if (distance_x < max_dist) and (distance_y < max_dist):
                    self.ship.alive = False
                    asteroid.alive = False

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        # TODO: Tell everything to advance or move forward one step in time
        for asteroid in self.asteroids:
            asteroid.advance()
            
        for bullet in self.bullets:
            bullet.advance()
        
        self.remove_notAliveObjects()
        self.check_collisions()
            
        self.ship.advance()

        # TODO: Check for collisions
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        :return:
        """

        # NOTE: This assumes you named your asteroids list "asteroids"    
       
    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.right()

        if arcade.key.UP in self.held_keys:
            self.ship.thrust()

        if arcade.key.DOWN in self.held_keys:
            self.ship.neg_thrust()

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
                bullet = Bullet(self.ship.angle, self.ship.center.x, self.ship.center.y)
                self.bullets.append(bullet)
                bullet.fire()

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()