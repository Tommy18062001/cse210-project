""" Bullet class for firing the laser. """

import arcade
from game import constants
from game.actor import Actor
import math
from game.sound import GameSound

class Bullet(Actor):
    """A template that will help us have a bullet for the game
    """
    
    def __init__(self):
        super().__init__()
        
        # velocity of the bullet 
        self.velocity.dx = constants.BULLET_SPEED
        self.velocity.dy = constants.BULLET_SPEED
        self.radius = constants.BULLET_RADIUS
        self.life = constants.BULLET_LIFE
        self.angle = 90
        
        # the look of the bullet
        self.img = "images/laser.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        # self.fire_bullet = GameSound(":resources:sounds/laser1.ogg", pan=-1.0)

    def __str__(self):
        """Player Bullet"""
        return #Player Bullet

    def fire(self, angle, ship):
        """ Controls the speed of the bullet. """
        self.velocity.dx = (math.cos(math.radians(angle - 270)) * constants.BULLET_SPEED) + (ship.velocity.dx / 2)
        self.velocity.dy = (math.sin(math.radians(angle - 270)) * constants.BULLET_SPEED) + (ship.velocity.dy / 2)
        # self.fire_bullet.play()
        return self.velocity.dx, self.velocity.dy

    def align_with_ship(self, ship):
        """ Orients the bullet in the direction the ship is facing."""
        self.center.x = ship.center.x
        self.center.y = ship.center.y
        self.angle += ship.angle - 90
        self.velocity.dx = (ship.velocity.dx + self.fire(ship.angle, ship)[0])
        self.velocity.dy = (ship.velocity.dy + self.fire(ship.angle, ship)[1])

    def draw(self):
        """ Draws bullet. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, constants.ALPHA)
