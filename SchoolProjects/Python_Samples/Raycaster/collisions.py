from data import *
from math import *
from vector_math import *

def sphere_intersection_point(ray, sphere):
	A = dot_vector(ray.dir, ray.dir)
	B = 2 * dot_vector(difference_point(ray.pt, sphere.center), ray.dir)
	C = (dot_vector(difference_point(ray.pt,sphere.center),
			difference_point(ray.pt,sphere.center)) - (sphere.radius**2))
	discriminant = (B ** 2.0 - 4.0 * A * C)

	if discriminant < 0:
		exit
	else:
		t1 = ((-B) + sqrt(discriminant)) / (2.0 * A)
		t2 = ((-B) - sqrt(discriminant)) / (2.0 * A)
		
		if t1 < 0 and t2 < 0:
			return None
		elif t1 >= 0 and t2 < 0:
			t1scaled = scale_vector(ray.dir, t1)
			realPt = translate_point(ray.pt, t1scaled)
		elif t1 < 0 and t2 >= 0:
			t2scaled = scale_vector(ray.dir, t2)
			realPt = translate_point(ray.pt, t2scaled)
		else:
			if t1 < t2:
				t1scaled = scale_vector(ray.dir, t1)
				realPt = translate_point(ray.pt, t1scaled)
			else:
				t2scaled = scale_vector(ray.dir, t2)
				realPt = translate_point(ray.pt, t2scaled)
		return realPt

def find_intersection_points(sphere_list, ray):
	return [(s, sphere_intersection_point(ray, s)) 
		 for s in sphere_list if sphere_intersection_point(ray, s) != None]

def sphere_normal_at_point(sphere, point):
	return normalize_vector(vector_from_to(sphere.center, point))
