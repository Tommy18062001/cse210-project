import math
from abc import abstractmethod
from game import constants
from game.point import Point
from game.velocity import Velocity


class FlyingObj:
    """ Base class for any flying object. """
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.radius = constants.SHIP_RADIUS
        self.angle = 0
        self.speed = 0
        self.direction = 1
        self.velocity.dx = math.cos(math.radians(self.direction)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.direction)) * self.speed

    @abstractmethod
    def __str__(self):
        pass

    def advance(self):
        """ Moves the objects forward. """
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    @abstractmethod
    def draw(self):
        """ To be implemented by child classes. """
        pass

    def wrap(self, screen_width, screen_height):
        """ Allows any flying object to wrap from one side of the screen to the other. """
        if self.center.x > screen_width:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = screen_width
        elif self.center.y > screen_height:
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = screen_height
