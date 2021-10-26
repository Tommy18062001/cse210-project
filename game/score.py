"""A class to keep track of the score"""

import arcade
from game import constants

class Score:
    """A template that will keep track of the score during the gameplay
    """
    def __init__(self):
        """The class constructor."""
        self.score = 0

    def update_score(self, value):
        """Add to current score."""
        self.score += value


    def display(self):
        """Display score"""
        score_text = "Score: {}".format(self.score)
        start_x = 20
        start_y = constants.SCREEN_HEIGHT - 30
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=16, color=arcade.color.WHITE)
        
    def get_score(self):
        """get the score"""
        return self.score
