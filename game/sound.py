"""A class for the sounds needed for the game."""

import arcade
from game import constants

class GameSound:
    """This will generate the gameplay sound. 
    """
    def __init__(self, sound_file, pan):
        self.sound = arcade.Sound(sound_file)
        self.pan = pan
        self.volume = constants.VOLUME

    def play(self):
        """ Play sound """
        self.sound.play(pan=self.pan, volume=self.volume)
