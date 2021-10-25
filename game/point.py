""" Point class for moving objects. """

class Point:
    """Represents distance from an origin (0, 0).

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance.
        _y (Point): The vertical distance.
    """
    
    def __init__(self):
        """The class constructor."""
        self.x = 0.0
        self.y = 0.0
        
    def get_x(self):
        """_x (integer): The horizontal distance."""
        return self.x
    
    def get_y(self):
        """_y (Point): The vertical distance."""
        return self.y