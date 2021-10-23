import arcade
from game.actor import Actor
from game.sound import GameSound
from game import constants
from abc import abstractmethod

class Asteroid(Actor):
    """ The class that will handle all the different size of asteroid and their behavior """
    def __init__(self):
        super().__init__()
        self.img = "images/asteroid.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width
        self.height = self.texture.height
        self.t_break = GameSound(":resources:sounds/explosion2.wav", pan=-1.0)

    def draw(self):
        """ Draws asteroids. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, constants.ALPHA)

    def move(self):
        """ Advances and spins asteroids. """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
           
    @abstractmethod
    def split(self, asteroid_list):
        pass

    def hit(self, asteroid_list):
        """ If hit, split and play sound. """
        self.split(asteroid_list)
        self.t_break.play()
        
    # Unlike the ship, the asteroid should bounce when the touch the screen
    def wrap(self, screen_width, screen_height):
        """ Responsible of the beaahvior of the asteroids when it touches the screen"""
        if self.center.x > screen_width or self.center.x < 0:
            self.velocity.dx *= -1
            self.velocity.dy *= 1
            
        if self.center.y > screen_height or self.center.y < 0:
            self.velocity.dx *= 1
            self.velocity.dy *= -1
        