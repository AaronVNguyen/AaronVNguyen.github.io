from data import *
from vector_math import *
from collisions import *

def convert_color(color):
	"""A function that converts a Color object with floats to a 
	   Color object with ints between [0,255].
	Attributes:
		color - a Color object"""
	color = Color(int(color.r * 255), int(color.g * 255), int(color.b * 255))
	if color.r > 255:
		color.r = 255
	if color.g > 255:
		color.g = 255
	if color.b > 255:
		color.b = 255
	return color

def add_to_color(color1, color2, color3 = Color()):
	"""A function that adds three colors together (for the purpose of diffusion
	and specular addition to a base color). Requires at least two colors.
	Attributes:
		color1, color2, color3 - all Color objects"""
	return Color(color1.r + color2.r + color3.r, 
		     color1.g + color2.g + color3.g,
		     color1.b + color2.b + color3.b)

def length_pt_to_pt(pt1, pt2):
	"""A function that returns the magnitude of the distance from pt1 to
	pt2.
	Attributes:
		pt1 = a Point object
		pt2 = a Point object"""
	return length_vector(vector_from_to(pt1, pt2))

def p_epsilon(sphere, point):
	"""A function that scales a sphere's normalized vector by .01 and
	returns a translated intersection point scaled by the normalized
	vector.
	Attributes:
		sphere - a Sphere object
		point - a Point object"""
	normVec = scale_vector(sphere_normal_at_point(sphere, point), .01)
	return translate_point(point, normVec)
	
def cast_ray(ray, sphere_list, ambientColor=Color(1.0, 1.0, 1.0), 
	     light=Light(), eyePosition=Point()):
	intersectionList = find_intersection_points(sphere_list, ray)
	emptyList = []

	if len(intersectionList) == len(emptyList):
		return Color(1.0, 1.0, 1.0)
	else:
		closestSphere = intersectionList[0][0]
		closestLength = length_pt_to_pt(ray.pt,intersectionList[0][1])
		intersectionPoint = intersectionList[0][1]

		for (sphere, point) in intersectionList:
			testLength = length_pt_to_pt(ray.pt,point)
			if closestLength > testLength:
				closestLength = testLength
				closestSphere = sphere
				intersectionPoint = point

                trueColor = Color((closestSphere.color.r * 
				  closestSphere.finish.ambient * ambientColor.r),
                                  (closestSphere.color.g * 
				  closestSphere.finish.ambient * ambientColor.g),
                                  (closestSphere.color.b * 
				  closestSphere.finish.ambient * ambientColor.b))

		#DIFFUSION CALCULATIONS
		pEpsilon = p_epsilon(closestSphere, intersectionPoint)
		sphereNorm = sphere_normal_at_point(closestSphere, intersectionPoint)
		pointLightNorm = normalize_vector(vector_from_to(pEpsilon, light.pt))
		lightVisibility = dot_vector(sphereNorm, pointLightNorm)
		
		addDiffuse = False
		diffuseValue = Color(light.color.r * lightVisibility * 
				       closestSphere.finish.diffuse * 
					 closestSphere.color.r,
				     light.color.g * lightVisibility * 
				       closestSphere.finish.diffuse * 
					 closestSphere.color.g,
				     light.color.b * lightVisibility * 
				       closestSphere.finish.diffuse * 
					 closestSphere.color.b)
		
		#CHECK FOR LIGHT VISIBILITY/OBSTRUCTION
		blocked = False
		ray_Pe = Ray(pEpsilon, pointLightNorm)
		blockIntersectionList = find_intersection_points(sphere_list,ray_Pe)
		lightDistance = length_pt_to_pt(pEpsilon,light.pt)

		for (sphere,point) in blockIntersectionList:
			if length_pt_to_pt(pEpsilon,point) < lightDistance:
				blocked = True

		if lightVisibility > 0:
			addDiffuse = True
		if blocked == True:
			addDiffuse = False

		#ADDING SPECULAR
		reflectionVector = Vector(pointLightNorm.x - 
					    (2 * lightVisibility) * sphereNorm.x,
					  pointLightNorm.y - 
					    (2 * lightVisibility) * sphereNorm.y,
					  pointLightNorm.z - 
					    (2 * lightVisibility) * sphereNorm.z)
		viewDir = normalize_vector(vector_from_to(eyePosition,pEpsilon))
		specularIntensity = dot_vector(reflectionVector, viewDir)
		specularValue = Color(0,0,0)

		if specularIntensity > 0:
			specContribNoLight = (closestSphere.finish.specular * 
						specularIntensity ** 
						  (1 / closestSphere.finish.roughness))
			specularValue = Color(light.color.r * specContribNoLight,
					      light.color.g * specContribNoLight,
					      light.color.b * specContribNoLight)

                if addDiffuse == False:
                        return add_to_color(trueColor, specularValue)
                else:
                        return add_to_color(trueColor, diffuseValue, specularValue)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height,
		  eye_point, sphere_list, ambientColor, light=Light()):

	imageFile = open('image.ppm', 'w')
	pointList = []
	xIncrement = (max_x - min_x) / float(width)
	yIncrement = (max_y - min_y) / float(height)

	for h in range(height):
		for w in range(width):
			pointList.append(Point((min_x + xIncrement*w),
					       (max_y - yIncrement*h)))
	eyeRay = [Ray(eye_point, vector_from_to(eye_point, point)) 
		  for point in pointList]

	imageFile.write('P3\n')
	imageFile.write(str(width) + ' ' + str(height) + '\n')
	imageFile.write('255\n')
	for ray in eyeRay:
		castRay = convert_color(cast_ray(ray, sphere_list, 
						 ambientColor, light, eye_point))
		imageFile.write(str(castRay.r) + ' ' + 
				str(castRay.g) + ' ' + 
				str(castRay.b) + '\n')
