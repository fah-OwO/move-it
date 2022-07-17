from screenApi import ScreenApi
import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront
import numpy
from fpsController import getDirection

scene = pywavefront.Wavefront(r'cathedral\source\combined02.obj', collect_faces=True)

scene_box = (scene.vertices[0], scene.vertices[0])
for vertex in scene.vertices:
	min_v = [min(scene_box[0][i], vertex[i]) for i in range(3)]
	max_v = [max(scene_box[1][i], vertex[i]) for i in range(3)]
	scene_box = (min_v, max_v)

scene_size     = [scene_box[1][i]-scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 5
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(scene_box[1][i]+scene_box[0][i])/2 for i in range(3)]

def getBuffer(scene):
	vertex_Data = [[[scene.vertices[vertex_i] for vertex_i in face] for face in mesh.faces] for mesh in scene.mesh_list]
	vertex_np = numpy.array(vertex_Data, dtype="float32")
	return vertex_np.flat

vertex_Data = getBuffer(scene)

def Model():
	glPushMatrix()
	glScalef(*scene_scale)
	glTranslatef(*scene_trans)
	glDrawArrays(GL_TRIANGLES, 0, int(len(vertex_Data) / 3))
	glPopMatrix()

def init():
	display = (800,600)
	gluPerspective(45, (display[0] / display[1]), 1, 500.0)
	glTranslatef(0.0, 0.0, -10)
	glEnable(GL_DEPTH_TEST)
	glEnableClientState(GL_VERTEX_ARRAY)
	vertex_buffer_object = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
	glBufferData(GL_ARRAY_BUFFER, len(vertex_Data) * 4, numpy.array(vertex_Data, dtype="float32"), GL_DYNAMIC_DRAW)
	glVertexPointer(3, GL_FLOAT, 0, None)

def move(glTranslate):
	keyboardState = screenApi.getKeyboardDict()
	moveDirection = getDirection(keyboardState)
	glTranslate(*moveDirection)

def loop():
	move(glTranslate)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glColor(1,0,0)
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
	Model()
	glColor(1,1,1)
	glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
	Model()
	
import pygameScreen
screenApi = ScreenApi(pygameScreen)
screenApi.setInit(init)
screenApi.setLoop(loop)
screenApi.start()