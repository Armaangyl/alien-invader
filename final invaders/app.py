"""
Primary module for Alien Invaders

This module contains the main controller class for the Alien Invaders application. There
is no need for any additional classes in this module.  If you need more classes, 99% of
the time they belong in either the wave module or the models module. If you are unsure
about where a new class should go, post a question on Piazza.

Armaan Om Goyal (aog26), Aman Patel (adp226)
May 5, 2019
"""
from consts import *
from game2d import *
from wave import *


class Invaders(GameApp):
    """
    The primary controller class for the Alien Invaders application

    This class extends GameApp and implements the various methods necessary for processing
    the player inputs and starting/running a game.

        Method start begins the application.

        Method update either changes the state or updates the Play object

        Method draw displays the Play object and any other elements on screen

    Because of some of the weird ways that Kivy works, you SHOULD NOT create an
    initializer __init__ for this class.  Any initialization should be done in
    the start method instead.  This is only for this class.  All other classes
    behave normally.

    Most of the work handling the game is actually provided in the class Wave.
    Wave should be modeled after subcontrollers.py from lecture, and will have
    its own update and draw method.

    The primary purpose of this class is to manage the game state: which is when the
    game started, paused, completed, etc. It keeps track of that in an attribute
    called _state.

    INSTANCE ATTRIBUTES:
        view:   the game view, used in drawing (see examples from class)
                [instance of GView; it is inherited from GameApp]
        input:  the user input, used to control the ship and change state
                [instance of GInput; it is inherited from GameApp]
        _state: the current state of the game represented as a value from consts.py
                [one of STATE_INACTIVE, STATE_NEWWAVE, STATE_ACTIVE, STATE_PAUSED, STATE_CONTINUE, STATE_COMPLETE]
        _wave:  the subcontroller for a single wave, which manages the ships and aliens
                [Wave, or None if there is no wave currently active]
        _text:  the currently active message
                [GLabel, or None if there is no message to display]

    STATE SPECIFIC INVARIANTS:
        Attribute _wave is only None if _state is STATE_INACTIVE.
        Attribute _text is only None if _state is STATE_ACTIVE.

    For a complete description of how the states work, see the specification for the
    method update.

    You may have more attributes if you wish (you might want an attribute to store
    any score across multiple waves). If you add new attributes, they need to be
    documented here.

    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
        numkey: the number of keys pressed within the last frame (relevant)
        [it is an int>=0]
    """


    def start(self):
        """
        Initializes the application.

        This method is distinct from the built-in initializer __init__ (which you
        should not override or change). This method is called once the game is running.
        You should use it to initialize any game specific attributes.

        This method should make sure that all of the attributes satisfy the given
        invariants. When done, it sets the _state to STATE_INACTIVE and create a message
        (in attribute _text) saying that the user should press to play a game.
        """

        self._state = STATE_INACTIVE
        self._wave = None
        self.numkey = 0
        assert (self._state==STATE_INACTIVE or self._state==STATE_NEWWAVE or \
        self._state == STATE_ACTIVE or self._state == STATE_PAUSED or \
        self._state==STATE_COMPLETE or self._state==STATE_CONTINUE)
        self._score = GLabel()
        self._text = GLabel(text="Welcome! \n Press 'A' to Play!",
                            font_size=26, font_name='RetroGame.ttf', \
                            x=GAME_WIDTH/2.0, \
                            y=GAME_HEIGHT/2.0, halign='center', valign='middle',
                            linecolor = 'white', fillcolor = 'black')

    def update(self, timer):
        """
        Animates a single frame in the game.

        It is the method that does most of the work. It is NOT in charge of playing the
        game.  That is the purpose of the class Wave. The primary purpose of this
        game is to determine the current state, and -- if the game is active -- pass
        the input to the Wave object _wave to play the game.

        As part of the assignment, you are allowed to add your own states. However, at
        a minimum you must support the following states: STATE_INACTIVE, STATE_NEWWAVE,
        STATE_ACTIVE, STATE_PAUSED, STATE_CONTINUE, and STATE_COMPLETE.  Each one of these
        does its own thing and might even needs its own helper.  We describe these below.

        STATE_INACTIVE: This is the state when the application first opens.  It is a
        paused state, waiting for the player to start the game.  It displays a simple
        message on the screen. The application remains in this state so long as the
        player never presses a key.  In addition, this is the state the application
        returns to when the game is over (all lives are lost or all aliens are dead).

        STATE_NEWWAVE: This is the state creates a new wave and shows it on the screen.
        The application switches to this state if the state was STATE_INACTIVE in the
        previous frame, and the player pressed a key. This state only lasts one animation
        frame before switching to STATE_ACTIVE.

        STATE_ACTIVE: This is a session of normal gameplay.  The player can move the
        ship and fire laser bolts.  All of this should be handled inside of class Wave
        (NOT in this class).  Hence the Wave class should have an update() method, just
        like the subcontroller example in lecture.

        STATE_PAUSED: Like STATE_INACTIVE, this is a paused state. However, the game is
        still visible on the screen.

        STATE_CONTINUE: This state restores the ship after it was destroyed. The
        application switches to this state if the state was STATE_PAUSED in the
        previous frame, and the player pressed a key. This state only lasts one animation
        frame before switching to STATE_ACTIVE.

        STATE_COMPLETE: The wave is over, and is either won or lost.

        You are allowed to add more states if you wish. Should you do so, you should
        describe them here.

        Parameter timer: The time in seconds since last update
        Precondition: timer is a number (int or float)
        """
        self._dismiss_start()
        if self._state == STATE_ACTIVE:
            self.ActiveHelper(timer)
        if self._state == STATE_PAUSED:
            self.PausedHelper()
        if self._state == STATE_NEWWAVE:
            self.NewWaveHelper()
        if self._state == STATE_CONTINUE:
            self.ContinueHelper()
        if self._state == STATE_COMPLETE:
            self.CompleteHelper()

    def draw(self):
        """
        Draws:
        - welcome message,
        - alien waves,
        - bolts (both player and alien)
        - ship
        - score

        When the game state is not STATE_NEWAVE or STATE_ACTIVE,
        the method draws the text message.
        When the state is STATE_NEWWAVE the method draws the wave of Aliens.
        When the state is STATE_ACTIVE the method draws the bolts and score
        keeper.
        """
        if self._state == STATE_INACTIVE:
            self._text.draw(self.view)
        if self._state == STATE_ACTIVE:
            self._wave.draw(self.view)
            self._score.draw(self.view)
        elif self._state == STATE_NEWWAVE:
            self._wave.draw(self.view)
        self._text.draw(self.view)
        if self._state == STATE_ACTIVE:
            self._wave.draw(self.view)
            self._score.draw(self.view)
        elif self._state == STATE_NEWWAVE:
            self._wave.draw(self.view)


    # HELPER METHODS FOR THE STATES GO HERE
    def ActiveHelper(self, timer):
        """
        Helper function -
        - calls update
        - refreshes player score (when aliens are killed with bolts)
        - sets game state to STATE_PAUSED or STATE_COMPLETE depending

        Parameter timer: The time in seconds since last update function call
        Precondition: timer is a number (int or float)
        """
        a = self._wave
        a.update(timer, self.input)
        self._score.text = "Score: " + str(a.get_score())
        if a._lives == 0 or a._ship is None and a._winstate!=True:
            self._state = STATE_PAUSED
        elif a._winstate is True:
            self._state = STATE_COMPLETE

    def NewWaveHelper(self):
        """
        Creates
        - GLabel
        - Wave Object
        - score counter
        - lives counter
        - sets state as STATE_ACTIVE
        """
        self._text = GLabel()
        self._wave = Wave()
        self._score = GLabel(text="Score: " + str(self._wave.get_score()),
                             font_size=26, font_name='RetroGame.ttf', \
                             x=GAME_WIDTH/2.0, y=GAME_HEIGHT-20, \
                             halign='left', valign='middle'\
                             ,linecolor = 'white', fillcolor = 'black')
        self._lives = GLabel(text="Current Lives: " + str(self._wave.get_lives()),
                             font_size=26, font_name='RetroGame.ttf', \
                             x=GAME_WIDTH/2.0, y=GAME_HEIGHT-20, \
                             halign='right', valign='middle'\
                             ,linecolor = 'white', fillcolor = 'black')
        self._state = STATE_ACTIVE

    def contmsg(self,num):
        """
        displays the message to resume, and tells the player about lives left
        """
        self._text = GLabel(text="Press 'a' to Resume \n" \
                + str(num)+" Lives left",font_size=26, \
        font_name='RetroGame.ttf', x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0,
        halign='center',valign='middle')

    def PausedHelper(self): #aman - see if you can use contmsg to help this
        """
        Helper function - ends game if lives=0 or continues with display message
        """
        a = self._wave
        if a._lives == 0:
            self._state = STATE_COMPLETE
        elif a._lives > 0:
            self.contmsg(a._lives)

    def ContinueHelper(self):
        """
        Helper function:
        - Creates a new ship
        - Clears the GLabel
        - Sets game state to STATE_ACTIVE
        """
        self._text = GLabel()
        self._wave.set_ship(Ship())
        self._state = STATE_ACTIVE

    def CompleteHelper(self):
        """
        Helper function -
        - Creates a GLabel when the game ends to inform user of win/loss
        """
        a = self._wave._lives
        if a==0:
            self._text = GLabel(text="You Lost! \n 0 lives left",font_size=26,\
            font_name='RetroGame.ttf', \
            x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0, halign='center', \
            valign='middle')
        elif a>0 and a<4:
            self._text = GLabel(text="You Won! \n"+ \
            str(self._lives)+" lives left",font_size=26, \
            font_name='RetroGame.ttf', x=GAME_WIDTH/2.0, y=GAME_HEIGHT/2.0, \
            halign='center', valign='middle')
        else:
            self._text = GLabel(text="You Won!\nWith extra lives left",
            font_size=26, font_name='RetroGame.ttf', x=GAME_WIDTH/2.0,
            y=GAME_HEIGHT/2.0, halign='center', valign='middle')

    def _dismiss_start(self):
        """
        Helper function:
        - Dismisses welcome screen and starts the game
        - Determines whether a has been pressed then continues or starts game
        - (Records key_count value as press and stores it in numkey
        press: value of the key input by the user [int>=0]
        """
        if self._state == STATE_PAUSED or self._state == STATE_INACTIVE:
            press = 0
            if self.input.is_key_down('a'):
                press = self.input.key_count
            pressed = (press!=0 and self.numkey==0)
            if (pressed is True) and (self._state==STATE_PAUSED):
                self._state=STATE_CONTINUE
            elif pressed:
                self._state=STATE_NEWWAVE
            self.numkey = press
