import pygame


init = None
loop = None
screenSize = (800,600)
addKeyboardEvent = None
addKeyboardEvent = lambda x:print(x)

def getKeyName( key ):
	name = pygame.key.name(key)
	name = name . replace('left ','l')
	name = name . replace('right ','r')
	return name

def getEvent():
	events = pygame.event.get()
	e = []
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		elif event.type == pygame.KEYDOWN:
			e = ('press',getKeyName(event.key))
			addKeyboardEvent(e)
		elif event.type == pygame.KEYUP:
			e = ('release',getKeyName(event.key))
			addKeyboardEvent(e)

def start():
	pygame.init()
	pygame.display.set_mode(screenSize, pygame.DOUBLEBUF|pygame.OPENGL|pygame.RESIZABLE, )
	if init: init()
	while True:
		getEvent()
		if loop: loop()
		pygame.display.flip()
		pygame.time.wait(10)

if __name__ == "__main__":
	start()