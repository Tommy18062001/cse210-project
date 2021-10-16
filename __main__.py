import arcade
from game.director import Director
from game import constants

# Creates the game and starts it going
window = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
arcade.run()
