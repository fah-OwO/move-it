from OpenGL.GL import *

def main():
	from screenApi import ScreenApi

	def init():
		pass
	
	def loop():
		glClear(GL_COLOR_BUFFER_BIT)
		glBegin(GL_TRIANGLES)
		glColor3f( 1, 0, 0 )
		glVertex3f(-1, -1, 0)
		glColor3f( 0, 1, 0 )
		glVertex3f(1, -1, 0)
		glColor3f( 0, 0, 1 )
		glVertex3f(0, 1, 0)
		glEnd()

	screenApi = ScreenApi()
	screenApi.setInit(init)
	screenApi.setLoop(loop)
	screenApi.start()
if __name__ == '__main__':
	main()

# https://github.com/ddigiorg/pyopengl-cubes/blob/master/shader.py