from queue import Queue

class KeyboardState():
	def __init__(self):
		self.keyboardState = {}
		self.keyboardEventQueue = Queue()
		self.setDebounce( True )
		self.setHold( True )

	def getState(self):
		return self.keyboardState.copy()

	def getEvent(self):
		if self.haveEvent():
			return self.keyboardEventQueue.get()
		else:
			return None

	def haveEvent(self):
		return not self.keyboardEventQueue.empty()

	def addEvent(self, event):
		if self.debounce:
			event = debounce( event, self.keyboardState )
		if self.hold or event[0]!='hold':
			self.keyboardEventQueue.put(event)
	def getKeyboardEventList(self):
		with self.keyboardEventQueue.mutex:
			outList = list(self.keyboardEventQueue.queue)
			self.clearKeyboardEventQueue()
			return outList
	def clearKeyboardEventQueue(self):
		self.keyboardEventQueue.queue.clear()

	def setDebounce(self, debounce):self.debounce = debounce
	def setHold(self, hold):self.hold = hold

def debounce( event, keyboardState ):
	eventType, keyCode = event
	if eventType == 'release':
		keyboardState[keyCode] = 'release'
	elif eventType == 'press':
		if keyCode not in keyboardState:
			keyboardState[keyCode] = eventType
		elif keyboardState[keyCode] == 'release':
			keyboardState[keyCode] = 'press'
		elif keyboardState[keyCode] in ['press','hold']:
			keyboardState[keyCode] = 'hold'
		else:
			raise ValueError()
	else:
		raise ValueError()
	return keyboardState[keyCode], keyCode

