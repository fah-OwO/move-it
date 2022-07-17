from keyboardState import KeyboardState

class ScreenApi():
    def __init__(self, module = None):
        self._initInput()
        self._initOutput()
        self._initState()
        self.module = module

    def _initInput(self):
        self.init = None
        self.loop = None
        self.screenSize = (800,600)

    def _initOutput(self):
        self.getScreenSize = None
        self.getKeyboardEvent = None

    def _initState(self):
        self._initKeyboardState()

    def _initKeyboardState(self):
        self.keyboardState = KeyboardState()
        self.haveKeyboardEvent = self.keyboardState.haveEvent
        self.getKeyboardEvent = self.keyboardState.getEvent
        self.getKeyboardEventList = self.keyboardState.getKeyboardEventList
        self.getKeyboardDict = self.keyboardState.getState

    def setInit(self, func):self.init = func
    def setLoop(self, func):self.loop = func
    def setScreenSize(self, screenSize):self.screenSize = screenSize

    def start(self, module = None ):
        if module is None:
            if self.module is not None:module=self.module
            else:import kivyScreen as module
        screen = module
        screen.init = self.init
        screen.loop = self.loop
        screen.screenSize = self.screenSize
        screen.addKeyboardEvent = self.keyboardState.addEvent
        screen.start()

    

