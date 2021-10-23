"""A class for the ship data"""
import arcade
from game.actor import Actor
from game import constants

class Ship(Actor):
    """set the ship attributes and methods based off the flying object"""
    def __init__(self):
        super().__init__()
        self.img = "images/ship.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width / 2
        self.height = self.texture.height / 2
        self.center.x =  constants.SCREEN_WIDTH // 2 
        self.center.y = self.height // 2

    
    def __str__(self):
        """ Constructor. """
        return "Player Ship"

  
    def draw(self):
        """ Draw ship. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, constants.ALPHA)
            
    def move(self):
        self.center.x += self.velocity.dx

    def speed_control(self, thrust):
        # Speed limit for x
        vx = self.velocity.dx
        if vx > 5:
            self.velocity.dx = 5
        elif vx < -5:
            self.velocity.dx = -5
