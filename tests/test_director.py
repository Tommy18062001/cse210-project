"""Test code for the Director class"""

from game.director import *
import pytest


class TestDirector:
    """
    A code template for testing the Director class.
    """

    def test_check_keys(self):
        """
        Asserts this function checks for keys that are being held down.
        """
        director = Director()
        assert arcade.key.LEFT ==  self.ship.center.x - self.ship.center.x - 5
        assert arcade.key.RIGHT ==  self.ship.center.x - self.ship.center.x + 5

        pytest.main(["-v", "--tb=line", "-rN", "director_test.py"])



