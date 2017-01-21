from groups import *
from fade_math import *

def make_list_from_file(infile):
        """A function that will make a one dimensional list from a ppm file.
        Starts after the first three lines, since the first three lines defines
        a ppm file. It will skip extraneous line breaks.
        Attributes:
                infile - the input file"""
        pixelList = []

	index = 3
        for aLine in infile:
                try:
                        line = aLine.strip('\n').split(' ')
                        for value in line:
                                pixelList.append((int(value)))
			index += 1
                except:
                        print 'Line ' + str(index),
                        print 'is not formatted correctly ... skipping'
			index += 1
        return pixelList

def sort_list_from_file(width, height, infile):
	"""A function that uses the returned list from make_list_from_file()
	and returns a list sorted by <height> rows and <width> column per row.
	Attributes:
		width - the input file's width
		height - the input file's height
		infile = the input file"""
        pixelList = groups_of_3(make_list_from_file(infile))
        sortedList = []
        for i in range(height):
                tempList = []
                for j in range(width):
                        tempList.append(pixelList[j + i * width])
                sortedList.append(tempList)
        return sortedList

def write_new_image(infile, row, col, radius):
        outfile = open('faded.ppm', 'w')
	row = int(row)
	col = int(col)

        # writes header, width x height, color cap value to file
        header = infile.readline()
        width_height = infile.readline().strip('\n').split(' ')
        color_cap = infile.readline()

        width = int(width_height[0])
        height = int(width_height[1])

        outfile.write(header + str(width) + ' ' + str(height) + '\n' + color_cap)
      
        sortedList = sort_list_from_file(width, height, infile)

	# begin fade
        for i in range(len(sortedList)): # row
                for j in range(len(sortedList[i])): # pixels
                        distance = dist(i, j, row, col)
                        scaleVal = fade_scale_val(radius, distance)
                        sortedList[i][j] = [int(sortedList[i][j][0] * scaleVal),
                                            int(sortedList[i][j][1] * scaleVal),
                                            int(sortedList[i][j][2] * scaleVal)]
                        outfile.write(str(sortedList[i][j][0]) + ' ' +
                                      str(sortedList[i][j][1]) + ' ' +
                                      str(sortedList[i][j][2]) + '\n')
	infile.close()
	outfile.close()
