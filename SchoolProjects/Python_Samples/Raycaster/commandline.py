from cast import *
from sys import *

#function skips sphere if invalid

def check_initial_conditions(argv):
	"""A function that checks if argv has a minimum of two argument vectors."""
	if len(argv) < 2:
		print "Usage: python ray_caster.py <filename> [-eye x y z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
		exit()
	
def file_to_spherelist(inputFile):
	"""The input function. Takes a file and checks whether or not each line
	is malformed in some way with regards to how a sphere should be set. If
	it is, in any way, it will print every line where a Sphere is malformed
	and it will not add that Sphere to the list.
	Attributes:
		file - a file open for reading"""
	lineIndex = 1
	testList = []
	sphereList = []
	
	# attempts to convert a file to a Sphere list, skipping the invalid spheres
	for line in inputFile:
		testList.append(line.strip().split())
	for i in range(len(testList)):
		try:
			sphereList.append(Sphere(Point(float(testList[i][0]),	 # point
											       float(testList[i][1]), 
											       float(testList[i][2])), 
											 		 float(testList[i][3]),	 # radius
											 Color(float(testList[i][4]),	 # color
											       float(testList[i][5]), 
											       float(testList[i][6])), 
											Finish(float(testList[i][7]),  # finish
													 float(testList[i][8]), 
													 float(testList[i][9]),
													 float(testList[i][10]))))
			lineIndex += 1
		except:
			print 'Malformed sphere on line', lineIndex, '... skipping'
			lineIndex += 1
	return sphereList


def check_and_define_arguments(argv):
	# defaults
	min_x = -10
	max_x = 10
	min_y = -7.5
	max_y = 7.5
	width = 1024
	height = 768
	eye_point = Point(0.0,0.0,-14.0)
	ambient = Color(1.0,1.0,1.0)
	light = Light(Point(-100.0,100.0,-100.0), Color(1.5,1.5,1.5))
	
	allValues = []
	
	if '-eye' in argv:
		try:
			eyeIndex = argv.index('-eye')
			eye_point = Point(float(argv[index+1]),
					  float(argv[index+2]),
					  float(argv[index+3]))
		except:
			pass
	if '-view' in argv:
		try:
       	viewIndex = argv.index('-view')
       	min_x = float(argv[viewIndex+1])
       	max_x = float(argv[viewIndex+2])
       	min_y = float(argv[viewIndex+3])
       	max_y = float(argv[viewIndex+4])
       	width = int(argv[viewIndex+5])
       	height = int(argv[viewIndex+6])
		except:
			pass
	if '-light' in argv:
		try:
			lightIndex = argv.index('-light')
         		lightPt = Point(float(argv[lightIndex+1]),
					float(argv[lightIndex+2]),
					float(argv[lightIndex+3]))
			lightColor = Color(float(argv[lightIndex+4]),
					   float(argv[lightIndex+5]),
					   float(argv[lightIndex+6]))
            		light = Light(lightPt, lightColor)
		except:
			pass
	if '-ambient' in argv:
		try:
			ambIndex = argv.index('-ambient')
			ambient = Color(float(argv[ambIndex+1]),
					float(argv[ambIndex+2]),
					float(argv[ambIndex+3]))
		except:
			pass
		
	allValues.append([min_x,max_x,min_y,max_y,width,height]) #view
	allValues.append(eye_point)
	allValues.append(ambient)
	allValues.append(light)
		
	return allValues
