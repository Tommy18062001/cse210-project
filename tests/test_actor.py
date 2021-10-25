"""Test code for the Actor class"""

from game.actor import Actor
import pytest
from game import constants


class TestActor:
    """
        Code template for testing the Actor class. 
    """

    def test_screen_wrap(self):
        """ Asserts that any flying object wraps from one side of the screen to the other. """

        actor = Actor()
        actor.wrap()
        
        assert self.center.x <= constants.SCREEN_HEIGHT
        assert self.center.y <= constants.SCREEN_HEIGHT


    pytest.main(["-v", "--tb=line", "-rN", "test_actor.py"]) 