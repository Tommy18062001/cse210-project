import arcade
from game import constants
from game.ship import Ship
from game.bullet import Bullet
from game.score import Score


def game_over(is_over):
    """ Displays Game Over message when player is killed. """
    if is_over:
        text = "GAME OVER"
        start_x = constants.SCREEN_HEIGHT / 2
        start_y = constants.SCREEN_HEIGHT / 2
        arcade.draw_rectangle_outline(center_x=start_x + 100, center_y=start_y, width=120, height=40, color=arcade.color.WHITE, border_width=2)
        arcade.draw_text(text, start_x=start_x + 50, start_y=start_y - 10, font_size=16, color=arcade.color.WHITE)


class Director(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    This class will then call the appropriate functions of
    each of the above classes.
    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        # if no background image is set
        arcade.set_background_color(arcade.color.SMOKY_BLACK)

        # creates ship
        self.ship = Ship()
        
        # holds keyboard keys
        self.held_keys = set()
        
        # holds the bullet until they die
        self.bullets = list()
        self.alien_bullet = list()

        # sets background image as background texture
        self.background_image = "images/bg.jpg"
        self.bg_texture = arcade.load_texture(self.background_image)

        self.score = Score()

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # background image
        arcade.draw_texture_rectangle(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
                                      constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                      self.bg_texture, 0, 255)

        # draws bullets if they are alive
        for b in self.bullets:
            if b.alive:
                b.draw()
        for ab in self.alien_bullet:
            if ab.alive:
                ab.draw()
                
        # draws ship if it is alive
        if self.ship.alive:
            self.ship.draw()
        else:
            # calls game_over - clears if Enter is pressed
            game_over(True)
            
        # draw score
        self.score.display()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collisions()

      

        if self.ship.alive:
            # ship can move if alive
            self.ship.advance()
            self.ship.wrap(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)    
            
        for b in self.bullets:
            # moves and counts down life of bullets
            if b.alive:
                b.advance()
                b.wrap(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
                b.life -= 1
                if b.life <= 0:
                    b.alive = False

        for ab in self.alien_bullet:
            # moves and counts down life of bullets
            if ab.alive:
                ab.advance()
                ab.wrap(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
                ab.life -= 1
                if ab.life <= 0:
                    ab.alive = False

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle  += self.ship.turn

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle -= self.ship.turn

        if arcade.key.UP in self.held_keys:
            self.ship.speed_control("pos")

        if arcade.key.DOWN in self.held_keys:
            self.ship.speed_control("neg")
            
        
        # check that the ship doesn't go beyond the border
        if self.ship.center.x > constants.SCREEN_WIDTH:
            self.ship.center.x = constants.SCREEN_WIDTH
            
        if self.ship.center.y > constants.SCREEN_HEIGHT:
            self.ship.center.y = constants.SCREEN_HEIGHT
            
    def check_collisions(self):
        pass

    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.LEFT:
                self.held_keys.add(arcade.key.LEFT)

            if key == arcade.key.RIGHT:
                self.held_keys.add(arcade.key.RIGHT)

            if key == arcade.key.UP:
                self.held_keys.add(arcade.key.UP)

            if key == arcade.key.DOWN:
                self.held_keys.add(arcade.key.DOWN)
                
            # added since pressing UP + LEFT together prevents SPACE from firing bullets
            if key == arcade.key.LSHIFT:
                bullet = Bullet()
                bullet.align_with_ship(self.ship)
                self.bullets.append(bullet)

            if key == arcade.key.SPACE:
                bullet = Bullet()
                bullet.align_with_ship(self.ship)
                self.bullets.append(bullet)

        # If ship died, pressing ENTER makes ship regenerate.
        if key == arcade.key.ENTER:
            self.held_keys.add(arcade.key.ENTER)
            self.ship = Ship()
            # -100 points for resetting ship
            self.score.score -= 100

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)

        
        
        
