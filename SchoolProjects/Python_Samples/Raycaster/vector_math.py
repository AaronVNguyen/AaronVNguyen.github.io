import data
from math import *

def scale_vector(vector, scalar):
	"""A function that returns a new Vector object with the original Vector
	object scaled by a scalar.
	Attributes:
		vector - a Vector object 
		scalar - a float"""
	return data.Vector((vector.x * scalar),
			   (vector.y * scalar), 
			   (vector.z * scalar))

def dot_vector(vector1, vector2):
	"""A function that returns the dot product between two vectors.
	Attributes:
		vector1 - a Vector object
		vector2 - a Vector object"""
	return ((vector1.x * vector2.x) +
		(vector1.y * vector2.y) +
		(vector1.z * vector2.z))

def length_vector(vector):
	"""A function that returns the absolute length of a vector.
	Attributes:
		vector - a Vector object"""
	return sqrt((vector.x ** 2) + 
		    (vector.y ** 2) + 
		    (vector.z ** 2))

def normalize_vector(vector):
	"""A function that normalizes a vector.
	Attributes: 
		vector - (a Vector object)"""
	return scale_vector(vector, (1.0/length_vector(vector)))

def difference_point(point1, point2):
	"""A function that returns the difference between two points' 
	three arguments and inputs it into a new Vector object 
	(point1 - point2 : point2 pointing to point1).
	Attributes:
		point1 - a Point object
		point2 - a Point object"""
	return data.Vector((point1.x - point2.x),
			   (point1.y - point2.y),
			   (point1.z - point2.z))

def difference_vector(vector1, vector2):
	"""A function that returns the difference between two vectors' 
	three arguments and inputs it into a new Vector object 
	(vector1 - vector2).
	Attributes:
		vector1 - a Vector object
		vector2 - a Vector object"""
	return data.Vector((vector1.x - vector2.x),
			   (vector1.y - vector2.y),
			   (vector1.z - vector2.z))

def translate_point(point, vector):
	"""A function that returns a new Point object that was translated with
	a given vector.
	Attributes:
		point - a Point object
		vector - a Vector object"""
	return data.Point((point.x + vector.x),
			  (point.y + vector.y),
			  (point.z + vector.z))

def vector_from_to(from_point, to_point):
	"""A function that returns the vector between two objects and inputs it
	into a new Vector object (to_point - from_point).
	Attributes:
		from_point - a Point object
		to_point - a Point object"""
	return (difference_point(to_point, from_point))
