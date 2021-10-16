import arcade
import math
from game.object import FlyingObj
from game import constants

class Ship(FlyingObj):
    # set the ship attributes and methods based off the flying object
    def __init__(self):
        super().__init__()
        self.center.x =  constants.SCREEN_WIDTH / 2
        self.center.y = constants.SCREEN_HEIGHT / 2
        self.turn = constants.SHIP_TURN_AMOUNT
        self.img = "images/ship.png"
        self.texture = arcade.load_texture(self.img)
        self.width = self.texture.width / 2
        self.height = self.texture.height / 2

    def __str__(self):
        return "Player Ship"

    def draw(self):
        """ Draw ship. """
        arcade.draw_texture_rectangle(self.center.x, self.center.y,
                                      self.width, self.height,
                                      self.texture, self.angle, constants.ALPHA)

    def speed_control(self, thrust):
        """ Adjusts velocity dx/dy used for thrust. """
        if thrust == "pos":
            self.velocity.dx += math.cos(math.radians(self.angle + 90)) * constants.SHIP_THRUST_AMOUNT
            self.velocity.dy += math.sin(math.radians(self.angle + 90)) * constants.SHIP_THRUST_AMOUNT
        elif thrust == "neg":
            self.velocity.dx -= math.cos(math.radians(self.angle + 90)) * constants.SHIP_THRUST_AMOUNT
            self.velocity.dy -= math.sin(math.radians(self.angle + 90)) * constants.SHIP_THRUST_AMOUNT

        # Speed limit for x
        vx = self.velocity.dx
        if vx > 5:
            self.velocity.dx = 5
        elif vx < -5:
            self.velocity.dx = -5
        # Speed limit for x
        vy = self.velocity.dy
        if vy > 5:
            self.velocity.dy = 5
        elif vy < -5:
            self.velocity.dy = -5
