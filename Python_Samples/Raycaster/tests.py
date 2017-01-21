import unittest
import data
from vector_math import *
import collisions
import cast

# Defaults
# data.Point(x=0, y=0, z=0)
# data.Vector(x=0, y=0, z=0)
# data.Ray(pt=Point(), dir=Vector())
# data.Sphere(center=data.Point(), radius=0)

class TestData(unittest.TestCase):

#object tests
	def test_point1(self):
		p = data.Point()
		self.assertEqual(p.x, p.y, p.z)
	def test_point2(self):
		p = data.Point(-.5, 1, -1)
		self.assertEqual(p.x, -.5)
		self.assertEqual(p.y, 1)
		self.assertEqual(p.z, -1)

	def test_vector1(self):
		v = data.Vector() 
		self.assertEqual(v.x, v.y, v.z)
	def test_vector2(self):
		v = data.Vector(-.5, 1, -1)
		self.assertAlmostEqual(v.x, -.5)
		self.assertEqual(v.y, 1)
		self.assertEqual(v.z, -1)

	def test_ray1(self):
		ray = data.Ray()
		self.assertEqual(ray.pt.x, ray.dir.x, 0)
		self.assertEqual(ray.pt.x, ray.pt.y, ray.pt.z)
		self.assertEqual(ray.dir.x, ray.dir.y, ray.dir.z)		
	def test_ray2(self):
		ray = data.Ray(data.Point(-.5, 1, -1), data.Vector(-.5, 1, -1))
		self.assertEqual(ray.pt.x, ray.dir.x, -.5)
		self.assertEqual(ray.pt.y, ray.dir.y, 1)
		self.assertEqual(ray.pt.z, ray.dir.z, -1)

	def test_sphere1(self):
		sphere = data.Sphere()
		self.assertEqual(sphere.center.x, sphere.radius, 0)
		self.assertEqual(sphere.center.x, sphere.center.y, sphere.center.z)
	def test_sphere2(self):
		sphere = data.Sphere(data.Point(), 0)
		self.assertEqual(sphere.center.x, sphere.center.y, sphere.center.z)
		self.assertEqual(sphere.center.x, sphere.radius, 0)
	def test_sphere3(self):
		sphere = data.Sphere(data.Point(-.5, 1, -1), 1)
		self.assertEqual(sphere.center.x, -.5)
		self.assertEqual(sphere.center.y, 1)
		self.assertEqual(sphere.center.z, -1)
		self.assertEqual(sphere.radius, 1)
	def test_sphere4(self):
		sphere = data.Sphere(data.Point(), (-.5/2*3**2)*.25)
		self.assertEqual(sphere.center.x, 0)
		self.assertEqual(sphere.center.x, sphere.center.y, sphere.center.z)
		self.assertAlmostEqual(sphere.radius, -.5625)
	def test_sphere5(self):
		sphere = data.Sphere(data.Point(-.5, 1, -1), 0)
		self.assertEqual(sphere.radius, 0)

#HW2
#start of __eq__ tests
	def test_point_eq1(self):
		point1 = data.Point()
		point2 = data.Point()
		self.assertTrue(point1 == point2)
	def test_point_eq2(self):
		point1 = data.Point(-.5, 0, 1)
		point2 = data.Point(-.5, 0, 1)
		self.assertTrue(point1 == point2)
	def test_point_eq3(self):
		point1 = data.Point(.000001, .000001, .000001)
		point2 = data.Point(.000002, .000003, .000004) 
		#epsilon_equal to hundred-thousandths place
		self.assertTrue(point1 == point2)
	def test_point_eq4(self):
		point1 = data.Point(.000001, .000001, .000001)
		point2 = data.Point(.000002, .000002, .00002)
		self.assertFalse(point1 == point2)

	def test_vector_eq1(self):
		vector1 = data.Vector()
		vector2 = data.Vector()
		self.assertTrue(vector1 == vector2)
	def test_vector_eq2(self):
		vector1 = data.Vector(-.5, 0, 1)
		vector2 = data.Vector(-.5, 0, 1)
		self.assertTrue(vector1 == vector2)
	def test_vector_eq3(self):
		vector1 = data.Vector(.000001, .000001, .000001)
		vector2 = data.Vector(.000002, .000002, .000002)
		self.assertTrue(vector1 == vector2)
	def test_vector_eq4(self):
		vector1 = data.Vector(.000001, .000001, .000001)
		vector2 = data.Vector(.000002, .000002, .00002)
		self.assertFalse(vector1 == vector2)

	def test_ray_eq1(self):
		ray1 = data.Ray(data.Point(), data.Vector())
		ray2 = data.Ray(data.Point(), data.Vector())
		self.assertTrue(ray1 == ray2)
	def test_ray_eq2(self):
		ray1 = data.Ray(data.Point(-.5, 0, 1.0), data.Vector(-.5, 0, 1))
		ray2 = data.Ray(data.Point(-.5, 0, 1.0), data.Vector(-.5, 0, 1))
		self.assertTrue(ray1 == ray2)
	def test_ray_eq3(self):
		ray1 = data.Ray(data.Point(.000001, .000001, .000001))
		ray2 = data.Ray(data.Point(.000002, .000002, .000002))
		self.assertTrue(ray1 == ray2)
	def test_ray_eq4(self):
		ray1 = data.Ray(data.Point(.000001, .000001, .000001))
		ray2 = data.Ray(data.Point(.000002, .000002, .00002))
		self.assertFalse(ray1 == ray2)

	def test_sphere_eq1(self):
		sphere1 = data.Sphere()
		sphere2 = data.Sphere()
		self.assertTrue(sphere1 == sphere2)
	def test_sphere_eq2(self):
		sphere1 = data.Sphere(data.Point(-.5, 0, 1), 1)
		sphere2 = data.Sphere(data.Point(-.5, 0, 1), 1)
		self.assertTrue(sphere1 == sphere2)
	def test_sphere_eq3(self):
		sphere1 = data.Sphere(data.Point(.000001, .000001, .000001), .000001)
		sphere2 = data.Sphere(data.Point(.000002, .000002, .000002), .000002)
		self.assertTrue(sphere1 == sphere2)	
	def test_sphere_eq4(self):
		sphere1 = data.Sphere(data.Point(.000001, .000001, .000001), .00001)
		sphere2 = data.Sphere(data.Point(.000002, .000002, .000002), .00002)
		self.assertFalse(sphere1 == sphere2)

#start vector_math.py tests
	def test_scale_vector_1(self):
		v = data.Vector()
		s = 1
		self.assertEqual(scale_vector(v, s), data.Vector())
	def test_scale_vector_2(self):
		v = data.Vector(-.5, 0, 1)
		s = -1
		self.assertEqual(scale_vector(v, s), data.Vector(.5, 0, -1))
	def test_scale_vector_3(self):
		v = data.Vector(.0001, .0002, .0003)
		s = 2.5
		self.assertAlmostEqual(scale_vector(v, s).x, .00025)
		self.assertAlmostEqual(scale_vector(v, s).y, .0005)
		self.assertAlmostEqual(scale_vector(v, s).z, .00075)

	def test_dot_product_1(self):
		v1 = data.Vector()
		v2 = data.Vector()
		self.assertEqual(dot_vector(v1, v2), 0)
	def test_dot_product_2(self):
		v1 = data.Vector(1, 1, 1)
		v2 = data.Vector(2, 2, 2)
		self.assertEqual(dot_vector(v1, v2), 6)
	def test_dot_product_3(self):
		v1 = data.Vector(.45, .55, .65)
		v2 = data.Vector(-.65, -.55, -.45)
		self.assertAlmostEqual(dot_vector(v1, v2), -.8875)

	def test_length_vector_1(self):
		v = data.Vector()
		self.assertEqual(length_vector(v), 0)
	def test_length_vector_2(self):
		v = data.Vector(1, 1, 1)
		self.assertAlmostEqual(length_vector(v), 1.7320508)
	def test_length_vector_3(self):
		v = data.Vector(-.5, .01, .995)
		self.assertAlmostEqual(length_vector(v), 1.11360899)

	def test_normalize_vector_1(self):
		v = data.Vector(1, 2, 3)
		vTrue = data.Vector(.2672612, .53452248, .8017837)
		self.assertTrue(normalize_vector(v) == vTrue)
	def test_normalize_vector_2(self):
		v = data.Vector(-.01, .001, 0)
		vTrue = data.Vector(-.9950371923, .09950371, 0)
		self.assertTrue(normalize_vector(v) == vTrue)

	def test_difference_point_1(self):
		p1 = data.Point()
		p2 = data.Point()
		p3 = data.Point()
		self.assertTrue(difference_point(p1, p2) == p3)
	def test_difference_point_2(self):
		p1 = data.Point(5, 4, -2)
		p2 = data.Point(5, -5, -1)
		p3 = data.Point(0, 9, -1)
		self.assertTrue(difference_point(p1, p2) == p3)

	def test_difference_vector_1(self):
		v1 = data.Vector()
		v2 = data.Vector()
		v3 = data.Vector()
		self.assertTrue(difference_vector(v1, v2) == v3)
	def test_difference_vector_2(self):
		v1 = data.Vector(5, 4, -2)
		v2 = data.Vector(5, -5, -1)
		v3 = data.Vector(0, 9, -1)
		self.assertTrue(difference_vector(v1, v2) == v3)
	def test_difference_vector_3(self):
		v1 = data.Vector(5, 4, -2)
		v2 = data.Vector(5, -5, -1)
		v3 = data.Vector(0, 9, -.99)
		self.assertFalse(difference_vector(v1, v2) == v3)

	def test_translate_point_1(self):
		p = data.Point()
		v = data.Vector(-1, 0, 1)
		t = data.Point(-1, 0, 1)
		self.assertTrue(translate_point(p, v) == t)
	def test_translate_point_2(self):
		p = data.Point(-.01, .001, 5)
		v = data.Vector(.01, -.002, -.5)
		t = data.Point(0, -.001, 4.5)
		self.assertTrue(translate_point(p, v) == t)

	def test_translate_vector_from_to_1(self):
		f = data.Point()
		t = data.Point(1, -1, 1)
		ft = data.Vector(1, -1, 1)
		self.assertTrue(translate_point(f, t) == ft)
	def test_translate_vector_from_to_2(self):
		f = data.Point(-.01, .001, 5)
		t = data.Point(.01, -.002, -.5)
		ft = data.Vector(0, -.001, 4.5)
		self.assertTrue(translate_point(f, t) == ft)
	def test_translate_vector_from_to_3(self):
		f = data.Point(-.01, .001, 5)
		t = data.Point(.01, -.002, -.5)
		ft = data.Vector(.01, -.001, 4.6)
		self.assertFalse(translate_point(f, t) == ft)

#collisions, discriminant > 0
	#ray on left sphere edge pointing to right sphere edge
	#realPts = (-1,0,0), (1,0,0)
	def test_sphere_intersection_point1(self):
		ray = data.Ray(data.Point(-2,0,0), data.Vector(1,0,0))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		collision = collisions.sphere_intersection_point(ray,sphere)
		expected = data.Point(-1,0,0)
		self.assertEqual(collision, expected)
	#ray on the bottom-most point of the sphere pointing upwards
	#realPts = (0,-1,0), (0,1,0)
	def test_sphere_intersection_point2(self):
		ray = data.Ray(data.Point(0,-1,0), data.Vector(0,2,0))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(0,-1,0)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	#ray with origin closest to us on sphere pointing towards the background in z-axis
	#realPts = (0,0,-1), (0,0,1)
	def test_sphere_intersection_point3(self):
		ray = data.Ray(data.Point(0,0,-1), data.Vector(0,0,1))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(0,0,-1)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	#more complicated point-test
	#realPts = (-1,-1,-1), (1,1,1)
	def test_sphere_intersection_point4(self):
		ray = data.Ray(data.Point(-2,-2,-2), data.Vector(1,1,1))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		exptdPtCoord = -0.57735026919
		expected = data.Point(exptdPtCoord,exptdPtCoord,exptdPtCoord)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
#collisions, discriminant == 0
	#ray on bottom-left, pointing upwards toward sphere's left edge
	def test_sphere_intersection_point5(self):
		ray = data.Ray(data.Point(-1,-1,0), data.Vector(0,1,0))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(-1,0,0)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	#ray on top-left, pointing to the right towards sphere's upper edge
	def test_sphere_intersection_point6(self):
		ray = data.Ray(data.Point(-1,1,0), data.Vector(1,0,0))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(0,1,0)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	#ray on top with origin near us, pointing towards the background (z-axis) and crossing
	#top edge of sphere
	def test_sphere_intersection_point7(self):
		ray = data.Ray(data.Point(0,1,-1), data.Vector(0,0,1))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(0,1,0)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	#ray with origin below sphere and towards us pointed upward in y-axis
	def test_sphere_intersection_point8(self):
		ray = data.Ray(data.Point(0, -1, -1), data.Vector(0,1,0))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(0,0,-1)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	#complicated point
	def test_sphere_intersection_point9(self):
		ray = data.Ray(data.Point(0,0,0), data.Vector(1,1,1))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		exptedPt = 0.57735026919 
		expected = data.Point(exptedPt, exptedPt, exptedPt)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	def test_sphere_intersection_point10(self):
		ray = data.Ray(data.Point(-1,0,0), data.Vector(-1,0,0))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(-1,0,0)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	def test_sphere_intersection_point11(self):
		ray = data.Ray(data.Point(0,-1,0), data.Vector(1,0,0))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(0,-1,0)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
	def test_sphere_intersection_point12(self):
		ray = data.Ray(data.Point(0,0,1), data.Vector(0,-1,0))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		expected = data.Point(0,0,1)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), expected)
#collisions, discriminant < 0
	#simple no collision
	def test_sphere_intersection_point13(self):
		ray = data.Ray(data.Point(-2,-2,0), data.Vector(0,1,1))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), None)
	#more complicated, no collision
	def test_sphere_intersection_point14(self):
		ray = data.Ray(data.Point(-1,-1,-2), data.Vector(0,1,1))
		sphere = data.Sphere(data.Point(0,0,0), 1)
		self.assertEqual(collisions.sphere_intersection_point(ray,sphere), None)


#collisions, everything else
	#testing discriminant == 0
	def test_find_intersection_point1(self):
		sphereList = [data.Sphere(data.Point(0,0,0), 1), data.Sphere(data.Point(0,0,0), 2)]
		ray = data.Ray(data.Point(0,0,0), data.Vector(1,0,0))
		expected = [(sphereList[0], data.Point(1,0,0)), (sphereList[1], data.Point(2,0,0))]
		self.assertEqual(collisions.find_intersection_points(sphereList,ray), expected)
	#testing discriminant > 0 (2 intersection points, returning the closest)
	def test_find_intersection_point2(self):
		sphereList = [data.Sphere(data.Point(0,0,0), 1), data.Sphere(data.Point(0,0,0), 2)]
		ray = data.Ray(data.Point(-3,0,0), data.Vector(1,0,0))
		expected = [(sphereList[0], data.Point(-1,0,0)), (sphereList[1], data.Point(-2,0,0))]
		self.assertEqual(collisions.find_intersection_points(sphereList,ray), expected)
	#testing for discriminant < 0 (should not add to list)
	def test_find_intersection_point3(self):
		sphereList = [data.Sphere(data.Point(0,0,0), 1), data.Sphere(data.Point(5,5,5), 1)]
		ray = data.Ray(data.Point(0,0,0), data.Vector(1,0,0))
		#expected = [(sphereList[0], data.Point(1,0,0))]
		self.assertTrue(len(collisions.find_intersection_points(sphereList,ray)) == 1)

	def test_sphere_normal1(self):
		sphere = data.Sphere(data.Point(0,0,0), 1)
		point = data.Point(1,0,0)
		expected = data.Vector(1,0,0)
		self.assertEqual(collisions.sphere_normal_at_point(sphere,point), expected)
	def test_sphere_normal2(self):
		sphere = data.Sphere(data.Point(0,0,0), 1)
		point = data.Point(-1, 2.5, 3)
		expected = data.Vector(-.24806946, .62017367, .74420840)
		self.assertEqual(collisions.sphere_normal_at_point(sphere, point), expected)

#start of cast test
	def test_color1(self):
		color = data.Color()
		self.assertEqual(color.r, 0)
		self.assertEqual(color.r, color.g, color.b)
	def test_color2(self):
		color = data.Color(.222, .5, 1.0)
		self.assertEqual(color.r, .222)
		self.assertEqual(color.g, .5)
		self.assertEqual(color.b, 1.0)
	
	def test_sphere_color(self):
		sphere = data.Sphere(color = data.Color(.222, .5, 1.0))
		self.assertEqual(sphere.color.r, .222)
		self.assertEqual(sphere.color.g, .5)
		self.assertEqual(sphere.color.b, 1.0)

	def test_convert_color1(self):
		color = data.Color(1.0, 1.0, 1.0)
		expected = data.Color(255, 255, 255)
		self.assertEqual(cast.convert_color(color), expected)		
	def test_convert_color2(self):
		color = data.Color(0.001, .01, .125)
		expected = data.Color(0, 2, 31)
		self.assertEqual(cast.convert_color(color), expected)
	
	def test_add_to_color1(self):
		color1 = data.Color(.05, .05, .05)
		color2 = data.Color(.01, .02, .03)
		expected = data.Color(.06, .07, .08)
		self.assertEqual(cast.add_to_color(color1,color2), expected)
	def test_add_to_color2(self):
		color1 = data.Color(.02, .03, .99)
		color2 = data.Color(.9, .7, .3)
		color3 = data.Color(1, 1, 1)
		expected = data.Color(1.92, 1.73, 2.29)
		self.assertEqual(cast.add_to_color(color1, color2, color3), expected)

	def test_length_pt_to_pt1(self):
		pt1 = data.Point(5,0,0)
		pt2 = data.Point(10,0,0)
		self.assertEqual(cast.length_pt_to_pt(pt1, pt2), 5)
	def test_length_pt_to_pt2(self):
		pt1 = data.Point(-1, .5, 2)
		pt2 = data.Point(7, -2, .5)
		self.assertAlmostEqual(cast.length_pt_to_pt(pt1, pt2), 8.5146932)

	def test_p_epsilon(self):
		sphere = data.Sphere(data.Point(1,1,1), 1)
		point = data.Point(2,2,2)
		expected = data.Point(2.0057735, 2.0057735, 2.0057735)
		self.assertEqual(cast.p_epsilon(sphere,point), expected)

	def test_cast_ray1(self):
		#ray intersects both spheres at 2 points each, sphere1 closer
		#also an order test
		ray = data.Ray(data.Point(0,0,10), data.Vector(0,0,-1))
		sphere1 = data.Sphere(data.Point(0,0,0), 1, data.Color(1.0,0,0))
		sphere2 = data.Sphere(data.Point(0,0,-1), 1, data.Color(0,1.0,0))
		sphere_list = [sphere1, sphere2]
		expected = data.Color(1.0,0,0)
		self.assertEqual(cast.cast_ray(ray, sphere_list), expected)
		sphere_list = [sphere2, sphere1]
		self.assertEqual(cast.cast_ray(ray, sphere_list), expected)
	def test_cast_ray2(self):
		#ray intersects two spheres at one and two points, one from inside a sphere
		ray = data.Ray(data.Point(0,0,0), data.Vector(1,1,0))
		sphere1 = data.Sphere(data.Point(0,0,0), 1, data.Color(0,1.0,0))
		sphere2 = data.Sphere(data.Point(2,2,0), 1, data.Color(0,0,1.0))
		sphere_list = [sphere1, sphere2]
		expected = data.Color(0,1.0,0)
		self.assertEqual(cast.cast_ray(ray,sphere_list), expected)
	def test_cast_ray3(self):
		#ray intersects only one sphere at 1 point
		ray = data.Ray(data.Point(-1,-1,0), data.Vector(1,0,0))
		sphere1 = data.Sphere(data.Point(0,0,0), 1, data.Color(0,0,1.0))
		sphere2 = data.Sphere(data.Point(2,2,2), 2, data.Color(1.0,0,0))
		sphere_list = [sphere1, sphere2]
		expected = data.Color(0,0,1.0)
		self.assertEqual(cast.cast_ray(ray, sphere_list), expected) 
	def test_cast_ray4(self):
		#ray doesn't intersect any
		ray = data.Ray(data.Point(3,3,0), data.Vector(0,0,1))
		sphere1 = data.Sphere(data.Point(0,0,0), 1, data.Color(1.0,0,0))
		sphere2 = data.Sphere(data.Point(1,1,0), 1, data.Color(0,1.0,0))
		sphere_list = [sphere2, sphere1]
		expected = data.Color(1.0, 1.0, 1.0)
		self.assertEqual(cast.cast_ray(ray, sphere_list), expected)

	def test_finish1(self):
		finish = data.Finish(0.5,0.5,1.0,1.0)
		self.assertEqual(finish.ambient, 0.5)
		self.assertEqual(finish.diffuse, 0.5)
		self.assertEqual(finish.specular, 1.0)
		self.assertEqual(finish.roughness, 1.0)
	def test_finish2(self):
		finish = data.Finish(.111,.111,0,0)
		self.assertEqual(finish.ambient, .111)
                self.assertEqual(finish.diffuse, .111)
                self.assertEqual(finish.specular, 0)
                self.assertEqual(finish.specular, 0)

		

if __name__ == "__main__":
	unittest.main()
