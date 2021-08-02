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

LIFE_BAR_X = 60
LIFE_BAR_Y = SCREEN_HEIGHT - 20
LIFE_BAR_WIDTH = 100
LIFE_BAR_HEIGHT = 20

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
        self.center.x = LIFE_BAR_X
        self.center.y = LIFE_BAR_Y
        self.alive = True
        self._width = LIFE_BAR_WIDTH
        self.height = LIFE_BAR_HEIGHT
        self.color = arcade.color.GREEN
        self.angle = 0
     
    ''' This sets the width as a property to prevent changes '''
    @property
    def width(self):
        if self._width <= 0:
            return 0
        return self._width
    
    ''' This method draws the lifebar on the screen '''
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, self.width, self.height, self.color, self.angle)
        
    ''' The lifebar decreases as the asteroids hit the ship, and the ship disappears once the lifebar reaches zero (0) '''
    def life_lost(self):
        self._width -= 10
        if self._width == 0:
            self.alive = False

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
    
    ''' Returns the life status of FlyingObject '''
    def is_alive(self):
        return self.alive
    
    def advance(self):
        ''' Call the wrap method of a flying object '''
        self.wrap(SCREEN_WIDTH, SCREEN_HEIGHT)        
        ''' Movement of the Flying Objects '''
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
    def __init__(self, ship_angle, ship_x, ship_y):
        super().__init__("images/laserBlue01.png")
        self.radius = BULLET_RADIUS
        self.life = BULLET_LIFE
        self.speed = BULLET_SPEED
        self.angle = ship_angle - 90
        self.center.x = ship_x
        self.center.y = ship_y
    
    ''' The sets the movement of the bullets and kill off the bullet '''
    def advance(self):
        super().advance()
        self.life -= 1
        if self.life <= 0:
            self.alive = False
    
    ''' The bullet follows the angle and velocity of the ship when fired '''
    def fire(self):
        self.velocity.dx -= math.sin(math.radians(self.angle + 90)) * BULLET_SPEED
        self.velocity.dy += math.cos(math.radians(self.angle + 90)) * BULLET_SPEED
    
class Ship(FlyingObject):
    ''' Create a ship that is a flying object '''
    def __init__(self):
        super().__init__("images/playerShip1_orange.png")
        self.radius = SHIP_RADIUS
        self.center.x = SCREEN_WIDTH // 2
        self.center.y = SCREEN_HEIGHT // 2
        self.angle = 1
    
    ''' The ship turns left when the left arrow key is pressed '''
    def turn_left(self):
        self.angle += SHIP_TURN_AMOUNT
    
    ''' The ship turns right when the right arrow key is pressed '''
    def turn_right(self):
        self.angle -= SHIP_TURN_AMOUNT
    
    ''' The ship moves upward when the up arrow key is pressed '''
    def upward_thrust(self):
        self.velocity.dx -= math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy += math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
    
    ''' The ship moves downward when the down arrow key is pressed '''
    def downward_thrust(self):
        self.velocity.dx += math.sin(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        self.velocity.dy -= math.cos(math.radians(self.angle)) * SHIP_THRUST_AMOUNT
        
class Asteroid(FlyingObject, ABC):
    ''' Create a common interface for all astroid type '''
    def __init__(self, img):
        super().__init__(img)
        self.radius = 0.0
        self.point = 0
    
class SmallAsteroid(Asteroid):
    ''' Small Asteroids that is an asteroid'''
    def __init__(self):
        super().__init__("images/meteorGrey_small1.png")
        self.radius = SMALL_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
    
    ''' The asteroids spin over as it advances '''
    def advance(self):
        super().advance()
        self.angle += SMALL_ROCK_SPIN
    
    ''' The asteroid dies on collision with the ship and bullet '''
    def divide(self, asteroids):
        self.alive = False
        ''' The small asteroids have 10 points '''
        self.point = 10
    
class MediumAsteroid(Asteroid):
    ''' Middle Asteroids that is an asteroid'''
    def __init__(self):
        super().__init__("images/meteorGrey_med1.png")
        self.radius = MEDIUM_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
    
    ''' The asteroids spin over as it advances '''
    def advance(self):
        super().advance()
        self.angle += MEDIUM_ROCK_SPIN
    
    ''' The asteroid divdes into two small ones on collision with the ship and bullet '''
    def divide(self, asteroids):
        ''' Small asteroid 1 '''
        small1 = SmallAsteroid()
        small1.center.x = self.center.x
        small1.center.y = self.center.y
        small1.velocity.dy = self.velocity.dy + 1.5
        small1.velocity.dx = self.velocity.dx + 1.5
        
        ''' Small asteroid 2 '''
        small2 = SmallAsteroid()
        small2.center.x = self.center.x
        small2.center.y = self.center.y
        small2.velocity.dy = self.velocity.dy - 1.5
        small2.velocity.dx = self.velocity.dx - 1.5
        
        ''' add the two new asteroids to the asteroid class'''
        asteroids.append(small1)
        asteroids.append(small2)
        ''' Kill off the original medium asteroid '''
        self.alive = False
        ''' The small asteroids have 5 points '''
        self.point = 5
        
class LargeAsteroid(Asteroid):
    ''' Large Asteroids that is an asteroid'''
    def __init__(self):
        super().__init__("images/meteorGrey_big1.png")
        self.center.x = random.randint(1, 50)
        self.center.y = random.randint(1, 150)
        self.direction = random.randint(1, 50)
        self.radius = BIG_ROCK_RADIUS
        self.speed = BIG_ROCK_SPEED
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed
    
    ''' The asteroids spin over as it advances '''
    def advance(self):
        super().advance()
        self.angle += BIG_ROCK_SPIN
    
    ''' The asteroid divdes into two medium and a
        small asteroid on collision with the ship and bullet '''
    def divide(self, asteroids):
        ''' Medium asteroid 1 '''
        med1 = MediumAsteroid()
        med1.center.x = self.center.x
        med1.center.y = self.center.y
        med1.velocity.dy = self.velocity.dy + 2
        
        ''' Medium asteroid 2 '''
        med2 = MediumAsteroid()
        med2.center.x = self.center.x
        med2.center.y = self.center.y
        med2.velocity.dy = self.velocity.dy - 2
        
        ''' Small asteroid '''
        small = SmallAsteroid()
        small.center.x = self.center.x
        small.center.y = self.center.y
        small.velocity.dy = self.velocity.dy + 5
        
        ''' add the three new asteroids to the asteroid class'''
        asteroids.append(med1)
        asteroids.append(med2)
        asteroids.append(small)
        ''' Kill off the original large asteroid '''
        self.alive = False
        ''' The small asteroids have 1 point '''
        self.point = 1
     
    
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
        self.lifebar = LifeBar()
        self.score = 0
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
            
        ''' Add  background of universe on the screen '''
        texture = arcade.load_texture("images/gameBackground.jpg")
        
        # TODO: draw each object        
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, texture, 0, 255)
        
        for asteroid in self.asteroids:
            asteroid.draw()
        
        for bullet in self.bullets:
            bullet.draw()
        
        if self.ship.alive:
            self.ship.draw()
        else:
            ''' Show game over message '''
            if not len(self.asteroids) == 0:
                self.game_status("Game Over!")
            else:
                self.game_status("You Win!")
            ''' Kill the lifebar '''
            self.lifebar.alive = False
            
        if self.lifebar.alive:
            self.lifebar.draw()
        
        ''' if ship is alive and all asteroids die, Kill the ship '''
        if self.ship.alive and len(self.asteroids) == 0:
            self.ship.alive = False
        
        self.draw_score()
  
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
        
        
        self.remove_deadObjects()
        self.check_collisions()
        
        self.ship.advance()
        
    # TODO: Check for collisions
    """
    Checks to see if bullets have hit targets.
    Updates scores and removes dead items.
    :return:
    """

    # NOTE: This assumes you named your asteroids list "asteroids"    
    def check_collisions(self):
        for bullet in self.bullets:
             for asteroid in self.asteroids:
                 ''' Make sure the bullet and asteroid are alive before checking for a collision '''
                 if (bullet.alive and asteroid.alive):
                     distance_x = abs(asteroid.center.x - bullet.center.x)
                     distance_y = abs(asteroid.center.y - bullet.center.y)
                     max_dist = asteroid.radius + bullet.radius
                     if (distance_x < max_dist) and (distance_y < max_dist):
                         ''' On collision with the ship, asteroids divide '''
                         asteroid.divide(self.asteroids)
                         bullet.alive = False
                         asteroid.alive = False
                         ''' Score is calculated '''
                         self.score += asteroid.point
                         
        for asteroid in self.asteroids:
            ''' Make sure the ship and asteroid are alive before checking for a collision '''
            if (self.ship.alive and asteroid.alive):
                distance_x = abs(asteroid.center.x - self.ship.center.x)
                distance_y = abs(asteroid.center.y - self.ship.center.y)
                max_dist = asteroid.radius + self.ship.radius
                if (distance_x < max_dist) and (distance_y < max_dist):
                    ''' On collision with the ship, the asteroids divide and lifebar reduces '''
                    asteroid.divide(self.asteroids)
                    self.lifebar.life_lost()
                    asteroid.alive = False
                    self.score -= asteroid.point
                    ''' Once lifebar is 0, the ship dies '''
                    if (not self.lifebar.alive):
                        self.ship.alive = False
    
    ''' Remove dead objects from the screen '''
    def remove_deadObjects(self):
        ''' Remove dead bullets '''
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)
        
        ''' Remove dead asteroids '''
        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

    ''' draw a score on the top right of screen '''   
    def draw_score(self):
        ''' Puts the current score on the screen '''
        score_text = "Score: {}".format(self.score)
        start_x = SCREEN_WIDTH - 80
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x = start_x, start_y = start_y, font_size = 12, color = arcade.color.WHITE)
    
    ''' Get game status-- prints either you win or game over '''
    def game_status(self, message):
        game_message = message
        start_x = SCREEN_WIDTH // 2 - 50
        start_y = SCREEN_HEIGHT // 2
        arcade.draw_text(game_message, start_x=start_x, start_y=start_y, font_size= 25, color=arcade.color.WHITE, align="center")
       
    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        ''' Regenerate the ship and lifebar as it is initiated when enter key is pressed '''
        if arcade.key.ENTER in self.held_keys:
            if not self.ship.alive and not self.lifebar.alive:
                self.lifebar.__init__()
                self.ship.__init__()
        
        if arcade.key.LEFT in self.held_keys:
            self.ship.turn_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.turn_right()

        if arcade.key.UP in self.held_keys:
            self.ship.upward_thrust()

        if arcade.key.DOWN in self.held_keys:
            self.ship.downward_thrust()

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
            
            if key == arcade.key.LEFT:
                self.held_keys.add(arcade.key.LEFT)
                
            if key == arcade.key.RIGHT:
                self.held_keys.add(arcade.key.RIGHT)
                          
            if key == arcade.key.UP:
                self.held_keys.add(arcade.key.UP)
                
            if key == arcade.key.DOWN:
                self.held_keys.add(arcade.key.DOWN)
                
        ''' If ship died, pressing ENTER will resuscitate the ship '''
        if key == arcade.key.ENTER:
            self.held_keys.add(arcade.key.ENTER)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()