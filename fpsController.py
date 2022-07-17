import numpy
x,y,z = 1,1,1
speed = 0.1
accerel = 2
_dict ={
	'w' : (0,0,z),
	'a' : (x,0,0),
	's' : (0,0,-z),
	'd' : (-x,0,0),
	'space' : (0,-y,0),
	'lctrl' : (0,y,0),
}
def mulSpeed( v ):
	global speed
	speed *= v
_funcDict = {
	'shift' : lambda:mulSpeed(accerel),
	'lshift' : lambda:mulSpeed(accerel),
	'c' : lambda:mulSpeed(1/accerel),
}
_allDict = {}
for i in _dict:
	_allDict[i] = _dict
for i in _funcDict:
	_allDict[i] = _funcDict

_npDict = {key:numpy.array(value) for key,value in _dict.items()}

def canMove( char ):
	return char in _npDict

def canFunc( char ):
	return char in _funcDict

def func( char ):
	_funcDict[char]()

def di( char ):
	return _npDict[char]

def getDirection( char ):
	moveDirection = numpy.array((0,0,0))
	if isinstance(char, dict):return _getDirection( char )# if type(char) is dict:_getDirection( char )
	if canFunc(char):func(char)
	if canMove(char):moveDirection += di(char)
	return moveDirection * speed

def _getDirection(keyBoardDict):
	moveDirection = numpy.array((0,0,0))
	for i in _allDict:
		if i in keyBoardDict and keyBoardDict[i] in ['press','hold']:
			if canFunc(i):func(i)
			if canMove(i):moveDirection+=di(i)
	return moveDirection * speed