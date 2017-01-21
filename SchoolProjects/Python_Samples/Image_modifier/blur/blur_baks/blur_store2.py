import time
from math import *
from sys import *
from groups import *

# also checks default value
def check_initial_conditions(argv):
	if len(argv) < 2:
		print "Usage: python blur.py <input file> [neighbor reach]"
		exit()
	elif len(argv) == 2:
		return 4
	else:
		return argv[2]
def in_file(argv):
	try:
		f = open(argv[1], 'r')
		return f
	except:
		print 'Could not open "' + argv + '" for reading.'
		exit()

def avg_pixel(row_min, row_max, col_min, col_max, width, height, pixelList):
	avgPixel = [0,0,0]
	for i in range(max(row_min, 0), min(row_max, width)):
		for j in range(max(col_min, 0), min(col_max, height)):
			avgPixel[0] += int(pixelList[i][j][0])
			avgPixel[1] += int(pixelList[i][j][1])
			avgPixel[2] += int(pixelList[i][j][2])
			print 'j:', j
			time.sleep(.01)
		print 'i:', i
		time.sleep(.01)
	totalPixels = (row_max - row_min+1) * (col_max - col_min+1)
	for i in range(len(avgPixel)):
		avgPixel[i] /= totalPixels
	return avgPixel	
			
def process_image(infile, blur):
	# function breaks if there is a double space
	outfile = open('blurred.ppm', 'w')

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

	# begin blur
	for i in range(len(sortedList)): # row
		row_min = i - blur
		row_max = i + blur
		for j in range(len(sortedList[i])): # pixel
			col_min = j - blur
			col_max = j + blur
			avgPixel = avg_pixel(row_min, row_max, col_min, col_max, width, height, sortedList)
			outfile.write(str(avgPixel[0]) + ' ' +
				      str(avgPixel[1]) + ' ' + 
				      str(avgPixel[2]) + '\n')
def main(argv):
	blur = check_initial_conditions(argv)
	infile = in_file(argv)
	process_image(infile, int(blur))

if __name__ == '__main__':
	main(argv)
