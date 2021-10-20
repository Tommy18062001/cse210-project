"""The definition of the main function. It initializes a game object and starts the game"""

import arcade
from game.director import Director
from game import constants

# Creates the game and starts it going
window = Director(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
arcade.run()
