import utility

class Point:
	"""A class to define a point.
	Attributes: x, y, z"""
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z
	def __eq__(self, other):
		return (utility.epsilon_equal(self.x, other.x) and 
			utility.epsilon_equal(self.y, other.y) and
			utility.epsilon_equal(self.z, other.z))
class Vector:
	"""A class to define a vector.
	Attributes: x, y, z"""
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z
	def __eq__(self, other):
		return (utility.epsilon_equal(self.x, other.x) and
			utility.epsilon_equal(self.y, other.y) and
			utility.epsilon_equal(self.z, other.z))
class Ray:
	"""A class to define a ray.
	Attributes: 
		pt - a Point object
		dir - a Vector object"""
	def __init__(self, pt=Point(), dir=Vector()):
		self.pt = pt
		self.dir = dir
	def __eq__(self, other):
		return (self.pt == other.pt and
			self.dir == other.dir)
class Color:
	"""A class to define color.
	Attributes:
		r - a float
		g - a float
		b - a float"""
	def __init__(self, r=0, g=0, b=0):
		self.r = r
		self.g = g
		self.b = b
	def __eq__(self, other):
		return (utility.epsilon_equal(self.r, other.r) and
			utility.epsilon_equal(self.g, other.g) and
			utility.epsilon_equal(self.b, other.b))

class Finish:
	"""A class to define a finish.
	Attributes:
		ambient - a float
		diffuse - a float
		specular - a float
		roughness - a float"""
	def __init__(self, ambient=1.0, diffuse=0.0, specular = 0.0, roughness = 1.0):
		self.ambient = ambient
		self.diffuse = diffuse
		self.specular = specular
		self.roughness = roughness
	def __eq__(self, other):
		return (utility.epsilon_equal(self.ambient, other.ambient) and
			utility.epsilon_equal(self.diffuse, other.diffuse) and
			utility.epsilon_equal(self.specular, other.specular) and
			utility.epsilon_equal(self.roughness, other.roughness))

class Light:
	"""A class that defines a light.
	Attributes:
		pt - a Point object
		color - a Color object"""
	def __init__(self, pt=Point(), color=Color(1.0, 1.0, 1.0)):
		self.pt = pt
		self.color = color
	def __eq__(self, other):
		return (self.pt == other.pt and
			self.color == other.color)
			
class Sphere:
	"""A class to define a sphere.
	Attributes: 
		center (a Point object) 
		radius (a float)
		color (a Color object)"""
	def __init__(self, center=Point(), radius=0, color=Color(), finish=Finish()):
		self.center = center
		self.radius = radius
		self.color = color
		self.finish = finish
	def __eq__(self, other):
		return (self.center == other.center and
			utility.epsilon_equal(self.radius, other.radius) and
			self.color == other.color and
			self.finish == other.finish)
