import time
from sys import *
from groups import *

def check_initial_conditions(argv):
	if len(argv) < 2:
		print "Usage: python <input file>"
		exit()

def in_file(argv):
	try:
		f = open(argv[1], 'r')
		return f
	except:
		print 'Could not open "' + argv + '" for reading.'

def process_image(infile):
	outfile = open('hidden.ppm', 'w')

	# writes header, width x height, color cap value to file
	for i in range(3):
		outfile.write(infile.readline())

	pixelList = []
	for row in infile:
		pixelList.append(row.strip('\n').split(' '))
		pixelList = groups_of_3(pixelList)
		extra = []
		for i in range(len(pixelList)): #[0,0,0] [1,1,1]
			if len(pixelList[i]) == 3:
				newRed = min((int(pixelList[i][0]) + 
					      int(pixelList[i][0]) * 10), 255)

				# writes one pixel to the file with r,g,b as newRed
				for i in range(3):
					outfile.write(str(newRed) + ' ')
				outfile.write('\n')

				# checks if there were any extras in pixelList. if not, it will reset pixelList
				if len(pixelList) == 1:
					pixelList = []

			# adds any extras to the beginning of a new store list
			else:
				extra.append(pixelList[i])
				pixelList = extra
				#store = [x for x in extra]

def main(argv):
	check_initial_conditions(argv)
	infile = in_file(argv)
	process_image(infile)

if __name__ == '__main__':
	main(argv)
