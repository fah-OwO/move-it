import pygameScreen as screen
from OpenGL.GL import *
from OpenGL.GLU import *

class cube():
	vertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
	edges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
	quads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))

def wire(vertices, edges, ):
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

def solid(vertices, quads, ):
	glBegin(GL_QUADS)
	for quad in quads:
		for vertex in quad:
			glVertex3fv(vertices[vertex])
	glEnd()

def wireOnSolid(vertices, edges, quads):
	glPushAttrib(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_DEPTH_TEST)
	glColor3f(1,1,1)
	solid(vertices, quads, )
	glColor3f(1,0,0)
	wire(vertices, edges, )
	glPopAttrib()

def rotate():
	glRotatef(1, 1, 1, 1)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


def init():
	''' почти те же функции, инициализирующие работу с OpenGL '''
	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
	glTranslatef(0.0, 0.0, -5)
	glEnable(GL_COLOR_MATERIAL)


def loop():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	rotate()
	wireOnSolid(cube.vertices, cube.edges, cube.quads, )
	

display = (400, 400)
	
if __name__ == '__main__':
	screen.init = init
	screen.loop = loop
	screen.screenSize = display
	screen.start()
