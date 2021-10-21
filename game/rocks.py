import arcade
import random
import math
from game.asteroid import Asteroid
from game import constants

class LargeRock(Asteroid):
    """
         This will help us display the rock during the gameplay
    """
    def __init__(self):
        super().__init__()
        
        # first of all, it's should be positioned randomnly
        self.center.x = random.randint(1, constants.SCREEN_WIDTH - 1)
        
        # we expect the rock to fall from the top and reach the bottom of the screen
        self.center.y = constants.SCREEN_HEIGHT
        
        self.direction = random.randint(1, 150)
        
        self.speed = constants.BIG_ROCK_SPEED
        
        self.velocity.dx = (math.cos(math.radians(self.direction)) * self.speed) * -1
        self.velocity.dy = (math.sin(math.radians(self.direction)) * self.speed) * -1
        
        self.radius = constants.BIG_ROCK_RADIUS
        
        self.point_value = 1

    def __str__(self):
        return "Large Asteroid"

    def split(self, asteroid_list):
        """ Splits when hit. """
        chunks = [MediumRock(), MediumRock(), SmallRock()]
        for each_chunk in chunks:
            each_chunk.center.x = self.center.x
            each_chunk.center.y = self.center.y
            
            # after the spliting process, add each chunck inside the list 
            asteroid_list.append(each_chunk)
            
        self.alive = False


class MediumRock(Asteroid):
    """ Sets variables for medium asteroids. """
    def __init__(self):
        super().__init__()
        
        # increase the speed of the rock when they are splited
        self.velocity.dx = random.uniform(-(constants.BIG_ROCK_SPEED + 0.5), (constants.BIG_ROCK_SPEED + 0.5))
        self.velocity.dy = random.uniform(-(constants.BIG_ROCK_SPEED + 0.5), (constants.BIG_ROCK_SPEED + 0.5))
        
        self.radius = constants.MEDIUM_ROCK_RADIUS
        self.spin_speed = constants.MEDIUM_ROCK_SPIN
        
        self.img = "images/asteroid.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width * 1.5
        self.height = self.texture.height * 1.5
        self.point_value = 2

    def __str__(self):
        return "Medium Asteroid"

    def split(self, asteroid_list):
        """ Splits when hit. """
        chunks = [SmallRock(), SmallRock()]
        for each_chunk in chunks:
            each_chunk.center.x = self.center.x
            each_chunk.center.y = self.center.y
            asteroid_list.append(each_chunk)
        self.alive = False


class SmallRock(Asteroid):
    """ Sets variables for small asteroids. """
    def __init__(self):
        super().__init__()
        
        self.velocity.dx = random.uniform(-(constants.BIG_ROCK_SPEED + 1), (constants.BIG_ROCK_SPEED + 1))
        self.velocity.dy = random.uniform(-(constants.BIG_ROCK_SPEED + 1), (constants.BIG_ROCK_SPEED + 1))
        
        self.radius = constants.SMALL_ROCK_RADIUS
        self.spin_speed = constants.SMALL_ROCK_SPIN
        
        self.img = "images/asteroid.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.point_value = 3

    def __str__(self):
        return "Small Asteroid"

    def split(self, asteroid_list):
        """ No splits. """
        self.alive = False