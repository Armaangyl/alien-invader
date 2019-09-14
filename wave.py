"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in the Alien
Invaders game.  Instances of Wave represent a single wave.  Whenever you move to a
new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on screen.
These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer.

Armaan Om Goyal (aog26), Aman Patel (adp226)
May 5, 2019
"""
from game2d import *
from consts import *
from models import *
import random


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.

    This subcontroller has a reference to the ship, aliens, and any laser bolts on screen.
    It animates the laser bolts, removing any aliens as necessary. It also marches the
    aliens back and forth across the screen until they are all destroyed or they reach
    the defense line (at which point the player loses). When the wave is complete, you
    should create a NEW instance of Wave (in Invaders) if you want to make a new wave of
    aliens.

    If you want to pause the game, tell this controller to draw, but do not update.  See
    subcontrollers.py from Lecture 24 for an example.  This class will be similar to
    than one in how it interacts with the main class Invaders.

    INSTANCE ATTRIBUTES:
        _ship:   the player ship to control [Ship]
        _aliens: the 2d list of aliens in the wave [rectangular 2d list of Alien or None]
        _bolts:  the laser bolts currently on screen [list of Bolt, possibly empty]
        _dline:  the defensive line being protected [GPath]
        _lives:  the number of lives left  [int >= 0]
        _time:   The amount of time since the last Alien "step" [number >= 0]

    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Invaders. It is okay if you do, but you MAY NOT ACCESS
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that
    you need to access in Invaders.  Only add the getters and setters that you need for
    Invaders. You can keep everything else hidden.

    You may change any of the attributes above as you see fit. For example, may want to
    keep track of the score.  You also might want some label objects to display the score
    and number of lives. If you make changes, please list the changes with the invariants.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        _direct:       determines the direction aliens are going [boolean]
        _direct_change:    determines when aliens change direction [boolean]
        _numkey:       the last key to be pressed [key on keyboard]
        _speed:        speed of the ship [int or float]
        _count:  a number value of the counter function [int>0]
        _count2: number value of the counter function [int>0]
        _speed:        a number value of the ships speed [int]
        _plyrbolts:    the number of player bolts on the screen [int == 1 or 0]
        _lives:        The number of lives the player has [int == 0,1,2,3]
        _lowht:       the lowht value for the alien height [int]
        _firerate:     the firerate of the powerUps [int]
        _winstate:       game state [boolean]
        _score:        the score of the game [int>=]
        _powerups:      a list containing PowerUp objects [1D list]
    """

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    def get_time(self):
        """
        Returns the time value
        """
        return self._time

    def get_bolts(self):
        """
        Returns the list of bolts
        """
        return self._bolts

    def get_PU(self):
        """
        Returns the list of powerups
        """
        return self._powerups

    def get_direct(self):
        """
        Returns the direction (boolean)
        """
        return self._direct

    def get_direct_change(self):
        """
        Returns the direct_change value (boolean)
        """
        return self._direct_change

    def get_numkey(self):
        """
        Returns the last key pressed in relevant time frame
        """
        return self._numkey

    def get_count(self):
        """
        Returns a number value (int) of the amount of counts (arbitrary)
        """
        return self._count

    def get_count2(self):
        """
        Returns a number value (int) of the amount of counts (arbitrary)
        """
        return self._count2

    def get_ship(self):
        """
        Returns ship object
        """
        return self._ship


    def get_speed(self):
        """
        Returns a number value (int) of the ships speed.
        """
        return self._speed

    def get_firerate(self):
        """
        Returns the fire rate value.
        """
        return self._firerate

    def get_lives(self):
        """
        Returns the number of player lives (int).
        """
        return self._lives

    def get_aliens(self):
        """
        Returns the 2-D list of Alien objects
        """
        return self._aliens

    def get_score(self):
        """
        Returns the score of the game (int)
        """
        return self._score

    def set_time(self, time):
        """
        Sets the time variable.

        Parameter _time: the amount of _time
        Precondition: _time is an int or float
        """
        self._time = time

    def set_PU(self, powerups):
        """
        Creates a list of powerups

        Parameter powerups: a list containing PowerUp objects
        Preconditions: powerups is a 1D list.
        """
        self._powerups=powerups

    def set_direct(self, direct):
        """
        Sets the direction .

        Parameter direct:  determines the direction that the aliens are going.
        Precondition: direct is a boolean with a True or False value.
        """
        self._direct = direct

    def set_direct_change(self, direct_change):
        """
        Sets the direct_change value.

        Parameter dirchange: true if it changes directions, false otherwise
        Precondition: direct_change is a boolean value
        """
        self._direct_change = direct_change

    def set_numkey(self, numkey):
        """
        Sets a specific key

        Parameter _numkey: the key to be pressed
        Precondition: is a key on the qwerty keyboard
        """
        self._numkey = numkey

    def set_count(self, count):
        """
        Sets a number value of the counter function.

        Parameter _count: the value of counter
        Precondition: is an int > 0
        """
        self._count = count

    def set_count2(self, count2):
        """
        Sets a number value of the counter function.

        Parameter _count: the value of counter
        Precondition: is an int > 0
        """
        self._count2 = count2

    def set_ship(self,ship):
        """
        Sets ship object

        Paremeter ship: the ship object
        Precondition: ship is a object of the Ship class.
        """
        self._ship = ship

    def set_speed(self, SHIP_MOVEMENT):
        """
        Sets a number value (int) of the ships speed.

        Parameter SHIP_MOVEMENT: constant speed inherited from consts.py
        Precondition: is a integer > 0
        """
        self._speed = SHIP_MOVEMENT

    def get_plyrbolts(self):
        """
        Returns the number of player bolts on the screen
        """
        return self._plyrbolts

    def set_plyrbolts(self, plyrbolts):
        """
        Sets the number of player bolts on the screen

        Parameter plyrbolts: the number of player bolts on the screen
        Precondition: plyrbolts int value equal to 0 or 1
        """
        self._plyrbolts = plyrbolts

    def set_lives(self, lives):
        """
        Sets the number of player lives (int).

        Parameter _lives: The number of lives the player has
        Precondition: is an int equal to 3, 2, 1, or 0
        """
        self._lives = lives

    def get_lowht(self):
        """
        Returns the lowht value for alien height
        """
        return self._lowht

    def set_lowht(self, lowht):
        """
        Sets the lowht value for alien height

        Parameter lowht: the lowht value for the alien height
        Precondition: lowht int equal to 700
        """
        self._lowht = lowht

    def set_firerate(self, firerate):
        """
        Sets the firerate of the powerUps

        Parameter firerate: int
        """
        self._firerate = firerate

    def set_winstate(self, winstate):
        """
        Sets winning game state

        Parameter winstate: if the player won or lost
        Precondition: winstate is True or False
        """
        self._winstate = winstate

    def set_score(self, score):
        """
        Sets the score of the game.

        Parameter _score: the score of the game.
        Precondition: score is an int >= 0. It only increases when aliens are killed.
                      Lose points when you die.
        """
        self._score = score

    def set_powerups(self,powerups):
        """
        sets bolts list

        Parameter _bolts: laser bolts on the screen
        Precondition: bolts is a list, possibly empty
        """
        self._powerups = powerups

    def set_bolts(self,bolts):
        """
        sets bolts list

        Parameter _bolts: laser bolts on the screen
        Precondition: bolts is a list, possibly empty
        """
        self._bolts = bolts

    def set_shooter(self,shooter):
        """
        sets shooter (arbitrary)

        Parameter _shooter: shooter alien
        Precondition: alien object
        """
        self._shooter = shooter

    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self):
        """
        Initializer method creates a single wave of Alien Invaders game
        """
        self.set_time(0)
        self.MakeAliens()
        self.set_ship(Ship())
        self.set_bolts([])
        self.set_powerups([])
        self.set_score(0)
        self.set_direct(True)
        self.set_direct_change(True)
        self.set_plyrbolts(0)
        self.set_lives(3)
        self.set_numkey(0)
        self.set_count(0)
        self.set_count2(0)
        self.set_lowht(GAME_HEIGHT)
        self.set_winstate(False)
        self.set_speed(SHIP_MOVEMENT)
        self.set_firerate(random.randint(1, BOLT_RATE)) #math.random?

    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self, timer, input):
        """
        Moves ship, aliens, and laser bolts

        Parameter timer: The time in seconds since last update call
        Precondition: timer is a number (int or float)

        Parameter input: the input from the keys
        Precondition: input is a valid key inputted by the user
        """
        a = self.get_ship()
        if a.x<=GAME_WIDTH-SHIP_WIDTH-1 and \
        input.is_key_down('right')==True:
            a.x+=self.get_speed()
        if a.x>SHIP_WIDTH and input.is_key_down('left')==True:
            a.x-=self.get_speed()
        press = 0
        self.MoveAliens(timer)
        if input.is_key_down('spacebar'):
            press = input.key_count
        pressed=(press!=0 and self._numkey==0)
        self.bolt_check()
        if pressed==True and self.get_plyrbolts()==0:
            self.get_bolts().append(Bolt(a.x, a.y))
        self.caller(press,timer)

    def bolt_check(self):
        """
        adds a player bolt if x.get_velocity exceeds 0
        """
        for x in self.get_bolts():
            if x.get_velocity() > 0:
                self.set_plyrbolts(1)

    def caller(self,press,timer):
        """
        calls the rest of the functions for update function
        """
        self.set_numkey(press)
        self.alien_fire()
        self.moveBolts(timer)
        self.deleteBolts()
        self.change_PU(timer)
        self.col_detectorPU()
        self.col_detector()
        self.GameState()

    # HELPER METHODS FOR COLLISION DETECTION
    def GameState(self):
        """
        Helper Function:
        - Sets the game state to win or loss depending on result
        - Removes aliens from list when hit by plyr bolt
        """
        a = self.get_aliens()
        num_of_aliens = ALIENS_IN_ROW * ALIEN_ROWS
        for i in a:
            for n in i:
                if n==None:
                    num_of_aliens-=1
        if num_of_aliens==0:
            self.set_winstate(True)
        for i in a:
            for n in i:
                if not n is None:
                    k = n.y - ALIEN_HEIGHT/2
                    if k < self.get_lowht():
                        self.set_lowht(k/2)
                    if self.get_lowht() < DEFENSE_LINE: #checks if aliens cross
                        self.set_lives(0)

    def MakeAliens(self):
        """
        Helper function:
        - creates list of Alien objects (2d)
        - positions list correctly in game window
        """
        self._aliens = []
        tot_x = ALIEN_H_SEP*2
        tot_y = GAME_HEIGHT-ALIEN_CEILING
        for i in reversed(range(ALIEN_ROWS)):
            alienrow = []
            for n in range(ALIENS_IN_ROW):
                if i % 6 == 0 or i % 6 == 1:
                    alienrow.append(Alien(tot_x, tot_y, "alien1.png"))
                elif i % 6 == 2 or i % 6 == 3:
                    alienrow.append(Alien(tot_x, tot_y, "alien2.png"))
                elif i % 6 == 4 or i % 6 == 5:
                    alienrow.append(Alien(tot_x, tot_y, "alien3.png"))
                tot_x+=ALIEN_WIDTH+ALIEN_H_SEP
            tot_x = ALIEN_H_SEP*2
            tot_y-=ALIEN_HEIGHT-ALIEN_V_SEP
            self.get_aliens().append(alienrow)

    def MoveAliens(self, timer):
        """
        Helper function:
        - Moves alien objects 1 step value after every timer value

        Parameter timer: The time in seconds since last update function call
        Precondition: timer is int or float type
        """
        orig = self.get_time()
        self.set_time(orig + timer)
        if self.get_time() >=ALIEN_SPEED:
            self.set_direct_change(False)
            self.MoveAliens_helper()
            if self.get_direct_change() == False:
                speed = ALIEN_H_WALK
                if self.get_direct():
                    self.move_horiz(speed)
                elif not self.get_direct():
                    self.move_horiz(-speed)
            c1 = self.get_count()+1
            c2 = self.get_count2()+1
            self.set_count(c1)
            self.set_count2(c2)
            self.set_time(0)

    def MoveAliens_helper(self):
        """
        helps MoveAliens set direction for aliens
        """
        for i in self.get_aliens():
            for n in i:
                if not n is None:
                    if n.x+ALIEN_H_WALK>=GAME_WIDTH-ALIEN_WIDTH/2.0 \
                    -ALIEN_H_SEP and self.get_direct():
                        self.set_direct(False)
                        self.set_direct_change(True)
                        self.move_vert()
                    elif n.x-ALIEN_H_WALK <= ALIEN_WIDTH/2.0+ALIEN_H_SEP \
                    and self.get_direct()==False:
                        self.set_direct(True)
                        self.set_direct_change(True)
                        self.move_vert()

    def move_vert(self):
        """
        Helper function: Moves the alien vertically across 2d list.
        """
        for i in self.get_aliens():
            for n in i:
                if not n is None:
                    n.y-=ALIEN_V_WALK

    def move_horiz(self, speed):
        """
        Helper function: Moves the alien horizontally across 2d list.
        """
        for i in self.get_aliens():
            for n in i:
                if not n is None:
                    n.x+=speed


    def alien_fire(self):
        """
        Helper function: determines the aliens that fire bolts to the player
        (fires when the arbitrary counter equals the random generated number)
        """
        a = self.get_aliens()
        shooter = None
        fired = False
        zero=0
        if self.get_count()==self.get_firerate():
            self.set_count(0)
            while not fired is True:
                max2=0
                alien_shooter = random.randint(0, ALIENS_IN_ROW-1)
                for i in range(len(a)):
                    for n in range(len(a[0])):
                        if a[i][n] == a[i][alien_shooter]:
                            max2 = a[i][n].y
                        elif a[i][n] is None:
                            pass
                        if zero < max2:
                            shooter = a[i][n]
                        fired = True
            self.get_bolts().append(Bolt(shooter.x, shooter.y))
            self.set_firerate(random.randint(1, BOLT_RATE))

    def firechecker(self): #is this needed? (Armaan)
        """
        Helper function: helps alien_fire determine shooter aliens
        """
        max1 = 0
        max2 = 0
        a = self.get_aliens()
        alien_shooter = random.randint(0, ALIENS_IN_ROW-1)
        for i in range(len(a)):
            for n in range(len(a[0])):
                if a[i][n] is None:
                    pass
                elif a[i][n] == a[i][alien_shooter]:
                    max2 = a[i][n].y
                    if max1 < max2:
                        self.set_shooter(a[i][n])
                    self.set_fired(True)

    def deleteBolts(self):
        """
        Deletes the bolt in the list if it goes outside the game heights
        """
        a = self.get_bolts()
        for i in self.get_bolts():
            if i.y>GAME_HEIGHT:
                a.remove(i)
                self.set_plyrbolts(0)
            elif i.y<=-BOLT_HEIGHT:
                a.remove(i)

    def moveBolts(self, timer):
        """
        Moves bolts in the list by the value of velocity

        Parameter timer: The time in seconds since last update function call
        Precondition: timer is int or float
        """
        for i in self.get_bolts():
            i.y+=i.get_velocity()

    def col_detector(self):
        """
        Helper function:
        - detects collisions on both aliens and ships
        - adds score dependant on the situation
        """
        rando = random.randint(1, powerup_RATE) #math method
        a = self.get_aliens()
        for i in self.get_bolts():
            if i.get_velocity()>0:
                for n in range(len(a)):
                    k = a[0]
                    for b in range(len(k)):
                        l = self.get_aliens()[n][b]
                        if not l is None:
                            col_checker = l.col_bolt(i)
                            self.col_detector_helper(i,n,b,l,col_checker,rando)
            else:
                col_checker = self.get_ship().col_alienbolt(i)
                if col_checker is True:
                    self.col_setter()
                    break #check if this is right?

    def col_detector_helper(self,i,n,b,l,col_checker,rando):
        """
        helps col_detector add score for elim aliens
        """
        if col_checker is True:
            if rando==random.randint(1, powerup_RATE):
                self.get_PU().append(PowerUp(l.x, l.y))
            if l.get_aliensource() == 'alien1.png':
                self.set_score(self.get_score() + 10)
            elif l.get_aliensource() == 'alien2.png':
                self.set_score(self.get_score() + 20)
            elif l.get_aliensource() == 'alien3.png':
                self.set_score(self.get_score() + 50)
            self.get_aliens()[n][b]=None
            if i in self.get_bolts():
                self.get_bolts().remove(i)
            self.set_plyrbolts(0)

    def col_detectorPU(self):
        """
        Helper function:
        - Detects if powerups collide with the ship.
        - Increments if speed of ship is < SHIP_SPEEDCEIL (refer constants)
        - Additionally, the power up gives the ship 1 extra life per powerup
        upto a limit of 6 lives in total.
        """
        for i in self.get_PU():
            col_checker = self.get_ship().col_powerup(i)
            if col_checker is True:
                if self.get_speed() < SHIP_SPEEDCEIL:
                    self.set_speed(self.get_speed() + 1)
                if self.get_lives()<=5:
                    self.set_lives(self.get_lives() + 1)
                self.get_PU().remove(i)

    def change_PU(self, timer):
        """
        Increases the speed when powerup is taken by ship, it also adds lives.

        Parameter timer: The time in seconds since last update function call
            Precondition: timer is int or float type
        """
        for i in self.get_PU():
            i.y+=i.get_velocity()
            if i.y<=powerup_HEIGHT:
                self.get_PU().remove(i)

    def col_setter(self):
        """
        Helper function, sets:
        Score,
        Ship,
        Bolts,
        Powerups,
        Speeds,
        Numplayer,
        Lives
        """
        self.set_score(self.get_score())
        self.set_ship(None)
        self.get_bolts().clear()
        self.get_PU().clear()
        self.set_speed(SHIP_MOVEMENT)
        self.set_plyrbolts(0)
        self.set_lives(self.get_lives() - 1)

    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self, view):
        """
        Draws the game objects to the view.

        Every single thing you want to draw in this game is a GObject.  To draw a GObject
        g, simply use the method g.draw(self.view).  It is that easy!

        Many of the GObjects(such as the ships, aliens, and bolts) are attributes in
        Wave. In order to draw them, you either need to add getters for these attributes
        or you need to add a draw method to class Wave.  We suggest the latter.  See
        the example subcontroller.py from class.
        """
        for i in self.get_aliens():
            for n in i:
                if not n is None:
                    n.draw(view)
        self.get_ship().draw(view)
        self.get_ship().get_linevalue().draw(view)
        for i in self.get_PU():
            i.draw(view)
        for i in self.get_bolts():
            i.draw(view)
