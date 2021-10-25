from game.point import Point
import pytest
from game import constants

class TestPoint:
    """
        Code template for testing the point class. 
    """
  
    def test_get_x(self):
        """Asserts the x point doesn't exceed the screen width
        """
        point = Point()
        point.get_x()
        assert point.x <= constants.SCREEN_WIDTH
        
    def test_get_y(self):
        """Asserts the y point doesn't exceed the screen height
        """
        point = Point()
        point.get_y()
        assert point.y <= constants.SCREEN_HEIGHT

pytest.main(["-v", "--tb=line", "-rN", "test_point.py"]) 