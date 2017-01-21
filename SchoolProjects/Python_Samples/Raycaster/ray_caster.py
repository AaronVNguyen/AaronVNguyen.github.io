from data import *
from sys import *
from cast import *
from commandline import *

# check if argv has enough arguments (2 minimum). Quits if it doesn't.

def main(argv):
	check_initial_conditions(argv)

	try:
		spheresFile = open(argv[1], 'r')
	except:
		print "Error. File does not exist or file cannot be read."
		exit()
	
	sphere_list = file_to_spherelist(spheresFile)

	# uses argv to check and define the values to cast
	castValues = check_and_define_arguments(argv)

	cast_all_rays(castValues[0][0],castValues[0][1],castValues[0][2],	# view
			        castValues[0][3],castValues[0][4],castValues[0][5],	# view
			        castValues[1],sphere_list,				# eye_point, sphere_list
			        castValues[2],castValues[3])				# ambient, light

if __name__ == '__main__':
	main(argv)
