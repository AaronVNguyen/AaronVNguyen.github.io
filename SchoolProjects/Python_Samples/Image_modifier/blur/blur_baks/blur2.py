import time
from math import *
from sys import *
from groups import *

def check_initial_conditions(argv):
	if len(argv) < 5:
		print "Usage: python fade.py <input file> <row> <col> <radius>"
		exit()

def in_file(argv):
	try:
		f = open(argv[1], 'r')
		return f
	except:
		print 'Could not open "' + argv + '" for reading.'
		exit()

def dist(pixel_r, pixel_c, row, col):
	return sqrt((int(row) - pixel_r) ** 2 +
		    (int(col) - pixel_c) ** 2)

def fade_scale_val(radius, distance):
	return max(((radius - distance) / float(radius)), 0.2)

def process_image(infile, row, col, radius):
	# function breaks if there is a double space
	outfile = open('faded.ppm', 'w')

	# writes header, width x height, color cap value to file
	header = infile.readline()
	width_height = infile.readline().strip('\n').split(' ')
	color_cap = infile.readline()

	width = int(width_height[0])
	height = int(width_height[1])

	outfile.write(header + str(width) + ' ' + str(height) + '\n' + color_cap)

	pixelList = [value.strip('\n').split(' ') for value in infile]

	# checks for misformatted file (if there is a random linebreak or a random double space)
	for values in pixelList:
		if '' in values:
			values.remove('')
		if ' ' in values:
			values.remove(' ')
	pixelList = groups_of_3(pixelList)

	# sort pixelList by rows, cols
	sortedList = []
	for i in range(height):
		tempList = []
		for j in range(width):
			tempList.append(pixelList[j + i * width])
		sortedList.append(tempList)

# all functional till here ---------------------------------------------------------------
	for i in range(len(sortedList)): # row
		for j in range(len(sortedList[i])): # pixels
			distance = dist(i+1, j+1, row, col)
#			print distance
			scaleVal = fade_scale_val(radius, distance)
#			print scaleVal
#			time.sleep(.5)
			sortedList[i][j] = [int(int(sortedList[i][j][0]) * scaleVal), 
					    int(int(sortedList[i][j][1]) * scaleVal),
					    int(int(sortedList[i][j][2]) * scaleVal)]
#--------------------------------------------------------------------------------------
			outfile.write(str(sortedList[i][j][0]) + ' ' +
				      str(sortedList[i][j][1]) + ' ' + 
				      str(sortedList[i][j][2]) + '\n')
def main(argv):
	check_initial_conditions(argv)
	infile = in_file(argv)
	radius = int(argv[4])
	process_image(infile, argv[2], argv[3], radius)

if __name__ == '__main__':
	main(argv)
