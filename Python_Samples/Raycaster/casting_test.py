from data import *
from cast import *

minX = -10
maxX = 10
minY = -7.5
maxY = 7.5
width = 1024
height = 768
eyePoint = Point(0, 0, -14)
ambient = Color(1.0, 1.0, 1.0)
pointLight = Light(Point(-100.0, 100.0, -100.0), Color(1.5, 1.5, 1.5))
sphereList = [Sphere(Point(1, 1, 0), 2, Color(0, 0, 1.0), Finish(0.2, 0.4, 0.5, 0.05)), 
	      Sphere(Point(0.5, 1.5, -3.0), .5, Color(1.0, 0, 0), Finish(0.4, 0.4, 0.5, 0.05))]
cast_all_rays(minX, maxX, minY, maxY, width, height, eyePoint, sphereList, ambient, pointLight)
