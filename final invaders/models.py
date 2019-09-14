"""
Models module for Alien Invaders

This module contains the model classes for the Alien Invaders game. Anything that you
interact with on the screen is model: the ship, the laser bolts, and the aliens.

Just because something is a model does not mean there has to be a special class for
it.  Unless you need something special for your extra gameplay features, Ship and Aliens
could just be an instance of GImage that you move across the screen. You only need a new
class when you add extra features to an object. So technically Bolt, which has a velocity,
is really the only model that needs to have its own class.

With that said, we have included the subclasses for Ship and Aliens.  That is because
there are a lot of constants in consts.py for initializing the objects, and you might
want to add a custom initializer.  With that said, feel free to keep the pass underneath
the class definitions if you do not want to do that.

You are free to add even more models to this module.  You may wish to do this when you
add new features to your game, such as power-ups.  If you are unsure about whether to
make a new class or not, please ask on Piazza.

Armaan Om Goyal (aog26), Aman Patel (adp226)
May 5, 2019
"""
from consts import *
from game2d import *

# PRIMARY RULE: Models are not allowed to access anything in any module other than
# consts.py.  If you need extra information from Gameplay, then it should be
# a parameter in your method, and Wave should pass it as a argument when it
# calls the method.


class Ship(GImage):
    """
    A class to represent the game ship.

    At the very least, you want a __init__ method to initialize the ships dimensions.
    These dimensions are all specified in consts.py.

    You should probably add a method for moving the ship.  While moving a ship just means
    changing the x attribute (which you can do directly), you want to prevent the player
    from moving the ship offscreen.  This is an ideal thing to do in a method.

    You also MIGHT want to add code to detect a collision with a bolt. We do not require
    this.  You could put this method in Wave if you wanted to.  But the advantage of
    putting it here is that Ships and Aliens collide with different bolts.  Ships
    collide with Alien bolts, not Ship bolts.  And Aliens collide with Ship bolts, not
    Alien bolts. An easy way to keep this straight is for this class to have its own
    collision method.

    However, there is no need for any more attributes other than those inherited by
    GImage. You would only add attributes if you needed them for extra gameplay
    features (like animation). If you add attributes, list them below.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        line: a GPath object [is a GPath object]
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)

    def get_linevalue(self):
        """
        Returns the line value.
        """
        return self._line

    def set_linevalue(self, line):
        """
        Sets the line value (horizontal alien defense line)

        Parameter line: A horizontal line on the screen between ship and aliens
            Precondition: line is an object instance of GRectangle class
        """
        self._line = line

    # INITIALIZER TO CREATE A NEW SHIP
    def __init__(self):
        """
        Initializes an Ship object with the given attributes.
        """
        self.set_linevalue(self.create_def_line())
        super().__init__(x=GAME_WIDTH/2, y=SHIP_BOTTOM,height=SHIP_HEIGHT,
                         width=SHIP_WIDTH, source='ship.png')

    def create_def_line(self):
        """
        Returns defense line with initialized Gpath attributes.
        """
        x = GPath(points=[0, DEFENSE_LINE, GAME_WIDTH, DEFENSE_LINE], \
        linewidth=2, linecolor='red')
        return x

    def col_powerup(self, powerup):
        """
        Returns True if the powerup collides with the ship.

        Parameter powerup: The powerup to check (imagesource is 'ship')
        Precondition: powerup is an instance of PowerUp class
        """
        x = powerup.x
        y = powerup.y
        col_checker = False
        if self.contains((x+powerup_WIDTH/2.0, y+powerup_HEIGHT/2.0)) or \
         self.contains((x-powerup_WIDTH/2.0, y+powerup_HEIGHT/2.0)) or \
         self.contains((x-powerup_WIDTH/2.0, y-powerup_HEIGHT/2.0)) or \
         self.contains((x+powerup_WIDTH/2.0, y-powerup_HEIGHT/2.0)) is True:
            col_checker = True
        if col_checker == True:
            return col_checker

    def col_bolt(self, bolt):
        """
        Returns True if the alien bolt collides with the ship

        Parameter bolt: The laser bolt to check
            Precondition: bolt is an instancee of Bolt class
        """
        x = bolt.x
        y = bolt.y
        col_checker = False
        if self.contains((x+BOLT_WIDTH/2.0, y+BOLT_HEIGHT/2.0)) or \
        self.contains((x-BOLT_WIDTH/2.0, y+BOLT_HEIGHT/2.0)) or \
        self.contains((x-BOLT_WIDTH/2.0, y-BOLT_HEIGHT/2.0)) or \
        self.contains((x+BOLT_WIDTH/2.0, y-BOLT_HEIGHT/2.0)):
            col_checker = True
        if col_checker is True:
            return col_checker


class Alien(GImage):
    """
    A class to represent a single alien.

    At the very least, you want a __init__ method to initialize the alien dimensions.
    These dimensions are all specified in consts.py.

    You also MIGHT want to add code to detect a collision with a bolt. We do not require
    this.  You could put this method in Wave if you wanted to.  But the advantage of
    putting it here is that Ships and Aliens collide with different bolts.  Ships
    collide with Alien bolts, not Ship bolts.  And Aliens collide with Ship bolts, not
    Alien bolts. An easy way to keep this straight is for this class to have its own
    collision method.

    However, there is no need for any more attributes other than those inherited by
    GImage. You would only add attributes if you needed them for extra gameplay
    features (like giving each alien a score value). If you add attributes, list
    them below.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        alien_source:  type of alien [source with image]
        pos_X:       x position of the alien[int>=0]
        pos_Y:       y position of the alien[int>=0]

    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def get_aliensource(self):
        """
        Returns the alien_source (image file).
        """
        return self.alien_source

    def setpos_X(self, pos_X):
        """
        Sets the pos_X coordinate position of the object on the x axis

        Parameter pos_X: numerical coordinate position along the x axis
            Precondition: x is int>=0
        """
        self.pos_X = pos_X

    def setpos_Y(self, pos_Y):
        """
        Sets the pos_Y coordinate position of the object on the y axis

        Parameter pos_Y: numerical coordinate position on y axis
            Precondition: y is int>=0
        """
        self.pos_Y = pos_Y

    def set_aliensource(self, alien_source):
        """
        Sets the alien_source.

        Parameter alien_source: the source image file for alien (Images folder)
            Precondition: alien_source is a valid .png image file in Images folder
        """
        self.alien_source = alien_source

    # INITIALIZER TO CREATE AN ALIEN
    def __init__(self, pos_X, pos_Y, alien_source):
        """
        Initializes an instance of Alien with attributes of
        x and y coordinates and source.

        Parameter pos_X: x position
        Precondition: pos_X isint>=0 and <=GAME_WIDTH

        Parameter pos_Y: y position
        Precondition: pos_Y is an int>=0 and <=GAME_HEIGHT

        Parameter alien_source: the source image file for alien (Images folder)
        Precondition: alien_source is a valid .png image file in Images folder
        """
        self.set_aliensource(alien_source)
        self.setpos_X(pos_X)
        self.setpos_Y(pos_Y)
        super().__init__(x=pos_X, y=pos_Y, width=ALIEN_WIDTH,
                         height=ALIEN_HEIGHT, source=alien_source)

    def col_bolt(self, bolt):
        """
        Returns True if ship bolt collides with the alien object

        Parameter bolt: The laser bolt to check
        Precondition: bolt is an object of Bolt class
        """
        x = bolt.x
        y = bolt.y
        col_checker = False
        if self.contains((x+BOLT_WIDTH/2.0, y+BOLT_HEIGHT/2.0)) or \
        self.contains((x-BOLT_WIDTH/2.0, y+BOLT_HEIGHT/2.0)) or \
        self.contains((x-BOLT_WIDTH/2.0, y-BOLT_HEIGHT/2.0)) or \
        self.contains((x+BOLT_WIDTH/2.0, y-BOLT_HEIGHT/2.0)) is True:
            col_checker = True
        if col_checker:
            return col_checker


class Bolt(GRectangle):
    """
    A class representing a laser bolt.

    Laser bolts are often just thin, white rectangles.  The size of the bolt is
    determined by constants in consts.py. We MUST subclass GRectangle, because we
    need to add an extra attribute for the velocity of the bolt.

    The class Wave will need to look at these attributes, so you will need getters for
    them.  However, it is possible to write this assignment with no setters for the
    velocities.  That is because the velocity is fixed and cannot change once the bolt
    is fired.

    In addition to the getters, you need to write the __init__ method to set the starting
    velocity. This __init__ method will need to call the __init__ from GRectangle as a
    helper.

    You also MIGHT want to create a method to move the bolt.  You move the bolt by adding
    the velocity to the y-position.  However, the getter allows Wave to do this on its
    own, so this method is not required.

    INSTANCE ATTRIBUTES:
        _velocity: The velocity in y direction [int or float]
        pos_X: The x position [int]
        pos_Y: the y position [int]

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        playerBolt: The bolt is coming from a player [Bolt object]
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def get_velocity(self):
        """
        Returns bolt velocity
        """
        return self._velocity

    def set_velocity(self,velocity): #NOT NEEDED - __init__
        """
        Sets bolt velocity
        """
        self._velocity = velocity

    # INITIALIZER TO SET THE VELOCITY
    def __init__(self, pos_X, pos_Y):
        """
        Initializes a Bolt object with the given attributes as shown
        (depends on whether the bolt.pos_Y is at SHIP_BOTTOM value)
        Parameter pos_X = x coordinate position
            Precondition = pos_X is int>=0 and <=GAME_WIDTH

        Parameter pos_Y = y coordinate position
            Precondition = pos_Y is int>=0 and <=GAME_HEIGHT
        """
        if pos_Y==SHIP_BOTTOM:
            super().__init__(x=pos_X, y=pos_Y+(BOLT_HEIGHT/2)+(SHIP_HEIGHT/2),
                             width=BOLT_WIDTH, height=BOLT_HEIGHT, \
                             fillcolor="red", linecolor="red")
            self.set_velocity(BOLT_SPEED)
            self.playerBolt = True
        else:
            super().__init__(x=pos_X, y=pos_Y-(BOLT_HEIGHT/2)-(ALIEN_HEIGHT/2),
                             width=BOLT_WIDTH, height=BOLT_HEIGHT, \
                             fillcolor="red", linecolor="red")
            self.set_velocity(-BOLT_SPEED)
            self.playerBolt = False

class PowerUp(GImage):
    """
    A subclass of GImage, PowerUp class represents a speed-life power up.
    PowerUp is represented as a rectangular box with value attributed in the
    constants file

    INSTANCE ATTRIBUTES:
        _velocity: The velocity in pos_Y direction (i.e. vertical)
        Precondition: velocity is int or float type
    """

    def get_velocity(self):
        """
        Returns the velocity of the powerup object of PowerUp class
        """
        return self._velocity

    def set_velocity(self, powerup_SPEED):
        """
        Sets the value of _velocity to be the constant powerup_SPEED
        """
        self._velocity = powerup_SPEED

    def __init__(self, pos_X, pos_Y):
        """
        Initializer method:
        - Creates a power up object with attributes initialized being
        pos X and pos Y
        - assigns value of velocity from constants file to _velocity

        Parameter pos_X = x coordinate position value
        Precondition: pos_X is int >=0 and <=GAME_WIDTH

        Parameter pos_Y = y coordinate position value
        Precondition: pos_Y is int>=0 and <=GAME_HEIGHT
        """
        super().__init__(x=pos_X,y=pos_Y-(ALIEN_HEIGHT/2)-(powerup_HEIGHT/2),
                         width=powerup_WIDTH,height=powerup_HEIGHT, \
                         source='ship.png')
        self.set_velocity(powerup_SPEED)
