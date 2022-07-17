from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.base import EventLoop
from kivy.clock import Clock

init = None
loop = None
screenSize = None # (800,600)
addKeyboardEvent = None
addKeyboardEvent = lambda x:print(x)

def getKeyName( key ):
	name = keycode[1]
	if name == 'space bar': name = 'space'
	return name

class CustomWidget(Widget):
	def __init__(self, **kwargs):
		super(CustomWidget, self).__init__(**kwargs)
		self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
		self._keyboard.bind(on_key_down=self._on_keyboard_down, on_key_up=self._on_keyboard_up)

	def _keyboard_closed(self):
		self._keyboard.unbind(on_key_down=self._on_keyboard_down, on_key_up=self._on_keyboard_up)
		self._keyboard = None
	def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
		event = ('press',getKeyName(keycode))
		self._addKeyboardEvent(event)
		return True
	def _on_keyboard_up(self, keyboard, keycode):
		event = ('release',getKeyName(keycode))
		self._addKeyboardEvent(event)
		return True
	def _addKeyboardEvent(self, event):
		if addKeyboardEvent:
			addKeyboardEvent(event)
	def update_glsl(self, nap):
		''' здесь меняем вершины и запускаем отрисовку '''
		if loop :loop()
		screenSize = Window.size
		Window.flip()

class MainApp(App):
	def build(self):
		root = CustomWidget()
		EventLoop.ensure_window()
		# if screenSize: Window.size = screenSize
		return root

	def on_start(self):
		Clock.schedule_interval(self.root.update_glsl, 40 ** -1) #это наш желательный FPS

def getScreenSize():
	return Window.size

def start():
	if init :init()
	MainApp().run()

if __name__ == '__main__':
	start()
