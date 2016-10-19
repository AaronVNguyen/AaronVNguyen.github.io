from groups import *

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

def write_new_image(infile):
        outfile = open('hidden.ppm', 'w')

        # writes header, width x height, color cap value to file
        for i in range(3):
                outfile.write(infile.readline())

	# begin puzzle solving
        pixelList = groups_of_3(make_list_from_file(infile))
        for aPixel in pixelList:
                newRed = min((aPixel[0] +
                             aPixel[0] * 10), 255)
                outfile.write(str(newRed) + ' ' +
                              str(newRed) + ' ' +
                              str(newRed) + '\n')
        infile.close()
        outfile.close()

