"""A class for the director of the game."""
import arcade
from game import constants
from game.asteroid import Asteroid
from game.ship import Ship
from game.bullet import Bullet
from game.score import Score
from game.rocks import LargeRock
from game.sound import GameSound

# Section of this code is from a smpale of the same game from Sburton42 link provided below.
#https://github.com/byui-burton/cs241p-course/blob/master/projects/asteroids/sample_code/asteroids.py
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
        
        # check if the game is over
        self.is_over = False
        
        # creates ship
        self.ship = Ship()
        
        # holds keyboard keys
        self.held_keys = set()
        
        # list of needed actor in order to make the play
        self.bullets = list()
        self.asteroids = list()

        # initialize the rock
        for i in range(3):
            asteroid = LargeRock()
            self.asteroids.append(asteroid)

        # set the background color 
        arcade.set_background_color(arcade.color.BUD_GREEN)
        
        # play a sound when the game is over
        self.dead_player = GameSound(":resources:sounds/gameover4.wav", pan=-1.0)

        self.score = Score()

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # draws bullets if they are alive
        for bullet in self.bullets:
            if bullet.alive:
                bullet.draw()
        
        for asteroid in self.asteroids:
            if asteroid.alive:
                asteroid.draw()
                
        # draws ship if it is alive
        if self.ship.alive:
            self.ship.draw()
        else:
            # calls game_over - clears if Enter is pressed
            self.is_over = True
            self.game_over(self.is_over)
            
        # draw score
        self.score.display()

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collisions()
        self.check_asteroid_free()

        if self.ship.alive:
            # ship can move if alive
            self.ship.move()
            self.ship.wrap(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)    
            
        for each_bullet in self.bullets:
            # moves and counts down life of bullets
            if each_bullet.alive:
                each_bullet.move()
                each_bullet.wrap(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
                each_bullet.life -= 1
                if each_bullet.life <= 0:
                    each_bullet.alive = False
          
        # generates more asteroids if total number is less than 4
        if len(self.asteroids) < 4:
            add_asteroid = LargeRock()
            self.asteroids.append(add_asteroid)
                      
        for asteroid in self.asteroids:
            # moves asteroids if alive
            if asteroid.alive:
                asteroid.move()
                asteroid.wrap(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
                
            else:
                self.asteroids.remove(asteroid)

        

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.center.x -= 5

        if arcade.key.RIGHT in self.held_keys:
            self.ship.center.x += 5
        
        # check that the ship doesn't go beyond the border
        if self.ship.center.x > constants.SCREEN_WIDTH:
            self.ship.center.x = constants.SCREEN_WIDTH
            
        if self.ship.center.x < 0:
            self.ship.center.x = 0
            
    def check_collisions(self):

        for asteroid in self.asteroids:

            # this will handle the collisions between the bullet and the asteroids
            for bullet in self.bullets:
                if bullet.alive and asteroid.alive:
                    bullet_collision = asteroid.radius + bullet.radius
                    
                    # check if the 
                    if abs(bullet.center.x - asteroid.center.x) < bullet_collision and abs(bullet.center.y - asteroid.center.y) < bullet_collision:
                        bullet.alive = False
                        asteroid.hit(self.asteroids)
                        self.score.update_score(asteroid.point_value)

            # this will handle the collisions between the ship and the asteroids
            if self.ship.alive and asteroid.alive:
                ship_collision = asteroid.radius + self.ship.radius
                if abs(self.ship.center.x - asteroid.center.x) < ship_collision and abs(self.ship.center.y - asteroid.center.y) < ship_collision:
                    self.ship.alive = False
                    
                    # play sound when player dies
                    self.dead_player.play()
    
    def check_asteroid_free(self):
        """Check all the asteroid that has passed beyond the border alive.
        It should afect the score of the player
        """
        for asteroid in self.asteroids:
            if asteroid.alive:
                if asteroid.center.y < 0:
                    if self.is_over:
                        pass
                    else:
                        self.score.score -= 10
                        asteroid.alive = False
                        
                        # make sure to remove the asteroid from the list
                        self.asteroids.remove(asteroid)

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
            self.score.score = 0
            
            # restart the game
            self.is_over = False

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
            
    def game_over(self, is_over):
        """ Displays Game Over message when player is killed. """
        if is_over:
            text = "GAME OVER"
            score = f"SCORE: {self.score.score}"
            start_x = constants.SCREEN_HEIGHT / 2
            start_y = constants.SCREEN_HEIGHT / 2
            arcade.draw_rectangle_outline(center_x=start_x + 100, center_y=start_y, width=160, height=40, color=arcade.color.WHITE, border_width=2)
            arcade.draw_text(text, start_x=start_x +  35, start_y=start_y - 10, font_size=16, color=arcade.color.WHITE)

            arcade.draw_rectangle_outline(center_x=start_x + 100, center_y=start_y - 40, width=160, height=40, color=arcade.color.WHITE, border_width=2)
            arcade.draw_text(score, start_x=start_x +  35, start_y=start_y - 50, font_size=16, color=arcade.color.WHITE)

        return is_over

        
        
        
