import arcade
from game import constants

class Score:
    """A template that will keep track of the score during the gameplay
    """
    def __init__(self):
        self.score = 0

    # add to current score
    def update_score(self, value):
        self.score += value

    def display(self):
        score_text = "Score: {}".format(self.score)
        start_x = 20
        start_y = constants.SCREEN_HEIGHT - 30
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=16, color=arcade.color.WHITE)
