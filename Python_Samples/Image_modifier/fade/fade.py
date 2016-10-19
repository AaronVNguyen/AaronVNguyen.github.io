from sys import *
from fade_commandline import *
from fade_file_funcs import *

def main(argv):
        check_initial_conditions(argv)
        infile = in_file(argv)
        radius = int(argv[4])
        write_new_image(infile, argv[2], argv[3], radius)

if __name__ == '__main__':
	main(argv)
